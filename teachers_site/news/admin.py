from django.contrib import admin
from .models import New, Commit

class CommitAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'get_description_commit', 'new']

    def get_description_commit(self, object):
        if len(object.description) > 20:
            return object.description[:17] + '...'
        return object.description

    get_description_commit.short_description = 'Описание'

class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description_new', 'publish']

    def get_description_new(self, object):
        if len(object.description) > 20:
            return object.description[:17] + '...'
        return object.description

    get_description_new.short_description = 'Описание'

admin.site.register(New, NewAdmin)

admin.site.register(Commit, CommitAdmin)
