# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin

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

class SuccessStory(CMSPlugin):
    storyId = models.CharField(max_length=10, default='Story ID')
    name = models.CharField(max_length=50, default='Candidate Name')
    excerpt = models.CharField(max_length=500, default='Excerpt')
    text = models.TextField(default='Story Content')
    image = models.ImageField(upload_to='success-stories/', default='success-stories/none.jpg')

class TeamMember(CMSPlugin):
    name = models.CharField(max_length=200, default='Name')
    title = models.CharField(max_length=400, default='Job Title')
    text = models.TextField(default='Description')
    image = models.ImageField(upload_to='team-members/', default='team-members/none.jpg')

class BoardMember(CMSPlugin):
    name = models.CharField(max_length=200, default='Name')
    title = models.CharField(max_length=400, default='Job Title')
    text = models.TextField(default='Description')

class Question(CMSPlugin):
    question = models.CharField(max_length=10000, default='Question')
    answer = models.TextField(default='Answer')
