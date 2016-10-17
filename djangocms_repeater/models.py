# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models.fields import PlaceholderField

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
    questionText = models.CharField(max_length=10000, default='Question')
    answerText = PlaceholderField('answerText')

HEADERCOLOURCHOICE = (
    ('W', 'White'),
    ('T', 'Teal'),
    ('O', 'Orange'),
    ('R', 'Red'),
)

HEADERALIGNMENTCHOICE = (
    ('L', 'Left'),
    ('C', 'Center'),
    ('R', 'Right'),
)

class SingleHeader(CMSPlugin):
    quoteText = models.CharField(max_length=500, default='Placeholder')
    backgroundImage = models.ImageField(upload_to='headers/', default='headers/none.jpg')
    colour = models.CharField(max_length=1, choices=HEADERCOLOURCHOICE, default='W')
    alignment = models.CharField(max_length=1, choices=HEADERALIGNMENTCHOICE, default='L')

class MultipleHeader(CMSPlugin):
    header_name = models.CharField(max_length=100, default='Slider')

class MultipleSingleHeader(CMSPlugin):
    quoteText = models.CharField(max_length=500, default='Placeholder')
    backgroundImage = models.ImageField(upload_to='headers/', default='headers/none.jpg')
    colour = models.CharField(max_length=1, choices=HEADERCOLOURCHOICE, default='W')
    alignment = models.CharField(max_length=1, choices=HEADERALIGNMENTCHOICE, default='L')

BUTTONCOLOURCHOICE = (
    ('teal', 'Teal'),
    ('orange', 'Orange'),
    ('red', 'Red'),
    ('blue', 'Blue'),
)

BUTTONTYPECHOICE = (
    ('d', 'Donate'),
    ('a', 'Apply Now'),
    ('l', 'Log in'),
    ('n', 'None')
)

class Button(CMSPlugin):
    buttonText = models.CharField(max_length=100, default='Button Text')
    buttonURL = models.URLField(blank=True)
    specialButton = models.CharField(max_length=1, choices=BUTTONTYPECHOICE, default='n')
    buttonColour = models.CharField(max_length=10, choices=BUTTONCOLOURCHOICE, default='blue')
