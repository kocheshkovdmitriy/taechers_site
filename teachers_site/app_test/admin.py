from django.contrib import admin
from .models import *

class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_cnt_task']

    def get_cnt_task(self, object):
        return len(object.tasks.all())

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'section', 'get_task']

    def get_task(self, object):
        if len(object.task) > 17:
            return object.task[:17] + '...'
        return object.task



admin.site.register(Section, SectionAdmin)
admin.site.register(Task, TaskAdmin)