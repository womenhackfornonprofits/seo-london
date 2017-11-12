# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from collections import OrderedDict

import django_filters
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.html import format_html
from seo_job.models import Job


def _choice_fn(field_name):
    return [
        (x[field_name], x[field_name])
        for x in
        Job.objects.published().values(field_name).distinct()
    ]


class JobBaseFilter(django_filters.FilterSet):

    q = django_filters.CharFilter(label='what', method='filter_q')
    loc = django_filters.CharFilter(label='where', method='filter_loc')
    company_name = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('company_name')
    )
    location = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('location')
    )
    job_function = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('job_function')
    )
    seniority = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('seniority')
    )

    class Meta:
        model = Job
        fields = ()

    def filter_icontain_fields(self, fields, queryset, name, value):
        if not value:
            return queryset
        values = [v.strip() for v in value.split()]

        for v in values:
            expression = models.Q()
            for field in fields:
                expression = expression | models.Q(
                    **{
                        '{}__iregex'.format(field):
                        r'\y{}\y'.format(re.escape(v))
                    }
                )
            queryset = queryset.filter(expression)
        return queryset

    def filter_q(self, queryset, name, value):
        return self.filter_icontain_fields([
            'job_title',
            'job_detail',
            'job_function',
            'summary'
        ], queryset, name, value)

    def filter_loc(self, queryset, name, value):
        return self.filter_icontain_fields([
            'location'
        ], queryset, name, value)


class JobFormFilter(JobBaseFilter):

    choice_filters = OrderedDict([
        ('company_name', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        }),
        ('location', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        }),
        ('job_function', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        }),
        ('seniority', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        })
    ])

    def __init__(self, data=None, queryset=None, **kwargs):
        super(JobFormFilter, self).__init__(data, queryset, **kwargs)
        self._update_filters()

    def _update_filter(self, field_name, update_values):
        kwargs = {
            attr_name: getattr(self.filters[field_name], attr_name)
            for attr_name in [
                'field_name', 'label', 'method', 'lookup_expr',
                'distinct', 'exclude',
            ]
        }
        kwargs.update(getattr(self.filters[field_name], 'extra'))
        kwargs.update(update_values)
        if isinstance(update_values['choices'], basestring):
            values = self.data.get(field_name, []) if self.data else []
            kwargs['choices'] = (
                getattr(self, update_values['choices'])(
                    field_name, values
                )
            )
        return django_filters.MultipleChoiceFilter(
            **kwargs
        )

    def _update_filters(self):
        # create the field for each filter
        [v.field for v in self.filters.values()]
        new_filters = OrderedDict()
        for k, v in self.choice_filters.items():
            new_filters[k] = self._update_filter(k, v)

        for k, v in new_filters.items():
            self.filters[k] = v
            if len(self.filters[k].extra['choices']) > 0:
                self.filters[k] = v
            else:
                del self.filters[k]

    def _partial_qs(self, field_name):
        qs = self.queryset
        data = self.data
        for name, filter_ in self.filters.items():
            value = data.get(name)
            if value is not None and field_name != name:
                qs = filter_.filter(qs, value)
        return qs

    def get_choices(self, field_name, values):
        qs = self._partial_qs(field_name)

        choice_qs = qs.exclude(
            **{field_name: ''}
        ).values(
            field_name
        ).annotate(
            counts=models.Count('id'),
            selected=models.Max(models.Case(
                models.When(
                    then=models.Value(1),
                    **{'{}__in'.format(field_name): values}
                ),
                default=models.Value(0),
                output_field=models.IntegerField()
            ))
        ).values(
            field_name, 'counts', 'selected'
        ).order_by(
            '-selected', '-counts',
        )

        if choice_qs.exists():
            choice_values = OrderedDict(
                (v[field_name], v['counts']) for v in choice_qs
            )
        else:
            choice_values = OrderedDict()

        left_over_choice_values = {
            (v, 0)
            for v in values if v not in choice_values.keys()
        } if values else {}

        if left_over_choice_values:
            choice_values.update(left_over_choice_values)
        choices = [
            (
                k, format_html('{} <span>({})</span>', k, v)
            )
            for k, v in choice_values.items()
        ]

        return choices
