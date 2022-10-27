from django.contrib import admin
from .models import *

class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_cnt_task']

    def get_cnt_task(self, object):
        return len(object.tasks.all())

    get_cnt_task.short_description = 'Количество заданий'

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'section', 'get_task']

    def get_task(self, object):
        if len(object.task) > 17:
            return object.task[:17] + '...'
        return object.task

    get_task.short_description = 'Условие'

class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_number_of_questions']

    def get_number_of_questions(self, object):
        return len(object.tasks_list.all())

    get_number_of_questions.short_description = 'Количество заданий в тесте'


admin.site.register(Section, SectionAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Test, TestAdmin)