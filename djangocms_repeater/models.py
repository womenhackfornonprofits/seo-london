# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin

@python_2_unicode_compatible
class Repeater(CMSPlugin):
    repeater_name = models.CharField(max_length=50)
    add_columns = models.BooleanField(default=False)

CAREERSTEPCHOICE = (
    ('b', 'Blue'),
    ('o', 'Orange'),
    ('w', 'White'),
)

class CareerStep(CMSPlugin):
    number = models.CharField(max_length=5, default='0')
    title = models.CharField(max_length=50, default='Step')
    description = models.CharField(max_length=300, default='', blank=True)
    style = models.CharField(max_length=1, choices=CAREERSTEPCHOICE, default='w')

LOGOCHOICE = (
    ('0', 'SEO London'),
    ('1', 'SEO Careers'),
    ('2', 'SEO Scholars'),
    ('3', 'SEO Connect'),
)

class Logo(CMSPlugin):
    logoChoice = models.CharField(max_length=1, choices=LOGOCHOICE, default='0')
