from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Question, SuccessStory

class MyModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Question, MyModelAdmin)


class StoryAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(SuccessStory, StoryAdmin)
