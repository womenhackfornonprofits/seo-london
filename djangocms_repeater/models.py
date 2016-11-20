# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

from cms.models import CMSPlugin

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

CAREERSTEPCHOICE = (
    ('b', 'Blue'),
    ('o', 'Orange'),
    ('w', 'White'),
)

LOGOCHOICE = (
    ('0', 'SEO London'),
    ('1', 'SEO Careers'),
    ('2', 'SEO Scholars'),
    ('3', 'SEO Connect'),
)


class Repeater(CMSPlugin):
    repeater_name = models.CharField(max_length=50)
    add_columns = models.BooleanField(default=False)


class CareerStep(CMSPlugin):
    number = models.CharField(max_length=5, default='0')
    title = models.CharField(max_length=50, default='Step')
    description = models.CharField(max_length=300, default='', blank=True)
    style = models.CharField(max_length=1, choices=CAREERSTEPCHOICE,
                             default='w')


class Logo(CMSPlugin):
    logoChoice = models.CharField(max_length=1, choices=LOGOCHOICE, default='0')


class SuccessStory(CMSPlugin):
    storyId = models.CharField(max_length=10, default='Story ID')
    name = models.CharField(max_length=50, default='Candidate Name')
    excerpt = models.CharField(max_length=500, default='Excerpt')
    storyImage = models.URLField(max_length=200, blank='True', default='http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png')


class TeamMember(CMSPlugin):
    name = models.CharField(max_length=200, default='Name')
    title = models.CharField(max_length=400, default='Job Title')
    image = models.URLField(max_length=200, blank='True', default='http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png')


class BoardMember(CMSPlugin):
    name = models.CharField(max_length=200, default='Name')
    title = models.CharField(max_length=400, default='Job Title')


class Question(CMSPlugin):
    questionText = models.CharField(max_length=10000, default='Question')


class SingleHeader(CMSPlugin):
    quoteText = models.CharField(max_length=150, default='Placeholder')
    captionText = models.CharField(max_length=200, default='', blank=True)
    backgroundImage = models.URLField(max_length=200, blank='True', default='http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png')
    colour = models.CharField(max_length=1, choices=HEADERCOLOURCHOICE, default='W')
    alignment = models.CharField(max_length=1, choices=HEADERALIGNMENTCHOICE, default='L')


class MultipleHeader(CMSPlugin):
    header_name = models.CharField(max_length=100, default='Slider')


class MultipleSingleHeader(CMSPlugin):
    quoteText = models.CharField(max_length=150, default='Placeholder')
    captionText = models.CharField(max_length=200, default='', blank=True)
    backgroundImage = models.URLField(max_length=200, blank='True', default='http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png')
    colour = models.CharField(max_length=1, choices=HEADERCOLOURCHOICE, default='W')
    alignment = models.CharField(max_length=1, choices=HEADERALIGNMENTCHOICE, default='L')


class Button(CMSPlugin):
    buttonText = models.CharField(max_length=100, default='Button Text')
    buttonURL = models.CharField(blank=True, default="/", max_length=100)
    specialButton = models.CharField(max_length=1, choices=BUTTONTYPECHOICE, default='n')
    buttonColour = models.CharField(max_length=10, choices=BUTTONCOLOURCHOICE, default='blue')


class Career(CMSPlugin):
    name = models.CharField(max_length=100, default='Career Name')
    careerURL = models.CharField(blank=True, default="/", max_length=100)
