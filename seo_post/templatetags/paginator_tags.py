# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain
from django import template

register = template.Library()


def calculate_pagination_numbers(
        number_of_pages, current_page_number,
        pages_before_after=2, pages_start_end=1, zero_one_index=1):

    current_page_number = current_page_number - zero_one_index
    length = pages_before_after * 2 + 1
    # if there are not enough pages
    if number_of_pages < length:
        return range(zero_one_index,
                     number_of_pages + zero_one_index)

    start = current_page_number - pages_before_after
    if start < 0:
        start = 0
    elif start >= number_of_pages - length:
        start = number_of_pages - length
    end = start + length

    pages_start = min(pages_start_end, start)
    pages_end = max(number_of_pages - pages_start_end,
                    end)
    has_start_gap = (start > pages_start_end)
    has_end_gap = (number_of_pages - end > pages_start_end)

    result = list(
        map(
            lambda x: x + zero_one_index
            if x is not None else None,
            chain(
                range(0, pages_start),
                [None] if has_start_gap else [],
                range(start, end),
                [None] if has_end_gap else [],
                range(pages_end, number_of_pages)
            )
        ))
    return result


@register.assignment_tag
def get_pagination_numbers(page_obj):

    if not page_obj:
        return []

    return calculate_pagination_numbers(
        page_obj.paginator.num_pages,
        page_obj.number
    )
