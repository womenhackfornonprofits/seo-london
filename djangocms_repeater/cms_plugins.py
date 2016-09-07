# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Repeater, CareerStep, Logo

class RepeaterPlugin(CMSPluginBase):
    model = Repeater
    name = 'Repeater Plugin'
    render_template = 'repeater_plugin/repeater.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(RepeaterPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(RepeaterPlugin)

class CareerStepPlugin(CMSPluginBase):
    model = CareerStep
    name = 'Career Step Plugin'
    render_template = "career_step.html"

    def render(self, context, instance, placeholder):
        context = super(CareerStepPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CareerStepPlugin)

class LogoPlugin(CMSPluginBase):
    model = Logo
    name = 'Logo Plugin'
    render_template = "logo.html"

    def render(self, context, instance, placeholder):
        context = super(LogoPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LogoPlugin)
