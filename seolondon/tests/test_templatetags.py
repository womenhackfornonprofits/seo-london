# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from seolondon.templatetags.paginator_tags import (
    calculate_pagination_numbers
)


class TestCalculatePagnation(unittest.TestCase):

    def test_calculate_pagination(self):
        tests = [
            ((4, 1),
             [1, 2, 3, 4]),
            ((3, 2),
             [1, 2, 3]),
            ((5, 6),
             [1, 2, 3, 4, 5]),
            ((10, 1),
             [1, 2, 3, 4, 5, None, 10]),
            ((10, 2),
             [1, 2, 3, 4, 5, None, 10]),
            ((10, 3),
             [1, 2, 3, 4, 5, None, 10]),
            ((10, 4),
             [1, 2, 3, 4, 5, 6, None, 10]),
            ((10, 5),
             [1, None, 3, 4, 5, 6, 7, None, 10]),
            ((10, 7),
             [1, None, 5, 6, 7, 8, 9, 10]),
            ((10, 9),
             [1, None, 6, 7, 8, 9, 10])
        ]
        for call_args, expected in tests:
            actual = calculate_pagination_numbers(*call_args)
            self.assertEqual(actual, expected)
