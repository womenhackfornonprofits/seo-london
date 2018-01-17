# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from collections import OrderedDict

import django_filters
from django.db import models
from django import forms
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect
from django.utils.html import format_html
from seo_job.models import Job


def _choice_fn(field_name):
    return [
        (x[field_name], x[field_name])
        for x in
        Job.objects.published().values(field_name).distinct()
    ]


class JobBaseFilter(django_filters.FilterSet):

    q = django_filters.CharFilter(
        label='what',
        method='filter_q',
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. Marketing'}
        )
    )
    loc = django_filters.CharFilter(
        label='where',
        method='filter_loc',
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. London'}
        )
    )
    industry = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('industry')
    )
    location = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('location')
    )
    seniority = django_filters.MultipleChoiceFilter(
        choices=lambda: Job.SENIORITY_CHOICES,
    )
    route = django_filters.MultipleChoiceFilter(
        name='application_route',
        label='Route',
        choices=lambda: Job.APPLICATION_ROUTE_CHOICES,
    )
    salary = django_filters.ChoiceFilter(
        label='Salary',
        choices=[
            (20000, '20000+'),
            (30000, '30000+'),
            (40000, '40000+'),
            (50000, '50000+'),
            (60000, '60000+'),
        ],
        method='filter_salary'
    )
    company_name = django_filters.MultipleChoiceFilter(
        choices=lambda: _choice_fn('company_name')
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
            'summary',
            'industry',
        ], queryset, name, value)

    def filter_loc(self, queryset, name, value):
        return self.filter_icontain_fields([
            'location'
        ], queryset, name, value)

    def filter_salary(self, queryset, name, value):
        return queryset.filter(
            models.Q(max_salary__gt=value) |
            models.Q(min_salary__gt=value)
        )


class JobFormFilter(JobBaseFilter):

    choice_filters = OrderedDict([
        ('industry', {
            'choices': 'get_choices_variable_list',
            'widget': CheckboxSelectMultiple,
        }),
        ('location', {
            'choices': 'get_choices_variable_list',
            'widget': CheckboxSelectMultiple,
        }),
        ('seniority', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        }),
        ('route', {
            'choices': 'get_choices',
            'widget': CheckboxSelectMultiple,
        }),
        ('salary', {
            'choices': 'get_salary_choices',
            'widget': RadioSelect,
        }),
        ('company_name', {
            'choices': 'get_choices_variable_list',
            'widget': CheckboxSelectMultiple,
        }),

    ])

    def __init__(self, data=None, queryset=None, **kwargs):
        super(JobFormFilter, self).__init__(data, queryset, **kwargs)
        self._update_filters()

    def _update_filter(self, filter_name, update_values):
        filter_class = self.filters[filter_name].__class__
        kwargs = {
            attr_name: getattr(self.filters[filter_name], attr_name)
            for attr_name in [
                'field_name', 'label', 'method', 'lookup_expr',
                'distinct', 'exclude',
            ]
        }
        kwargs.update(getattr(self.filters[filter_name], 'extra'))
        original_choices = kwargs.get('choices')
        field_name = kwargs.get('field_name')
        kwargs.update(update_values)
        if isinstance(update_values['choices'], basestring):
            values = self.data.get(filter_name, []) if self.data else []
            kwargs['choices'] = (
                getattr(self, update_values['choices'])(
                    filter_name, field_name, values, original_choices
                )
            )
        return filter_class(**kwargs)

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

    def _partial_qs(self, filter_name):
        qs = self.queryset
        data = self.data
        for name, filter_ in self.filters.items():
            value = data.get(name)
            if value is not None and filter_name != name:
                qs = filter_.filter(qs, value)
        return qs

    def get_choices(
            self, filter_name, field_name, values, original_choices=None):
        choice_fn = (
            dict(original_choices()).get
            if original_choices is not None
            else lambda x: x
        )
        qs = self._partial_qs(filter_name)

        choice_qs = qs.exclude(
            **{field_name: ''}
        ).values(
            field_name
        ).annotate(
            counts=models.Count('id'),
        ).order_by()

        choice_values = [
            (v[field_name], v['counts'], v[field_name] in values)
            for v in choice_qs
        ]

        field_names = [v[0] for v in choice_values]

        left_over_choice_values = [
            (v, 0, True)
            for v in values if v not in field_names
         ] if values else []

        if left_over_choice_values:
            choice_values.extend(left_over_choice_values)

        choice_values = sorted(
            choice_values,
            key=lambda x: (-x[2], -x[1])
        )
        choices = [
            (
                k, format_html('{} <span>({})</span>', choice_fn(k), v)
            )
            for k, v, selected in choice_values
        ]

        return choices

    def get_choices_variable_list(
            self, filter_name, field_name, values, original_choices=None):
        return self.get_choices(filter_name, field_name, values)

    def _cumulative_salary_counts(self, filter_name, field_name):
        qs = self._partial_qs(filter_name)
        default_choices = sorted(
            self.filters[filter_name].extra.get('choices'),
            key=lambda x: -x[0]
        )

        when_args = [
            models.When(
                models.Q(max_salary__gt=level) |
                models.Q(min_salary__gt=level),
                then=level
            )
            for (level, name) in default_choices
        ]

        choice_counts_qs = qs.annotate(
            salary_level=models.Case(
                *when_args,
                default=None,
                output_field=models.IntegerField()
            )
        ).values(
            'salary_level'
        ).annotate(
            counts=models.Count('id')
        ).order_by(
            'salary_level'
        )
        choice_counts_lookup = {
            x['salary_level']: x['counts']
            for x in choice_counts_qs
        }
        cum_total = 0
        for val, name in default_choices:
            cum_total += choice_counts_lookup.get(val, 0)
            yield val, name, cum_total

    def get_salary_choices(
            self, filter_name, field_name, values, original_choices=None):
        choices = []
        for val, name, cum_total in sorted(
                self._cumulative_salary_counts(filter_name, field_name),
                key=lambda x: x[0]):
            choices.append((val, format_html(
                '{} <span>({})</span>', name, cum_total
            )))
        return choices
