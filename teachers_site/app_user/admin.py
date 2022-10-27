from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_surname', 'city', 'school', 'grade']
    filter_horizontal = ['tests']

    def get_name(self, object):
        return object.user.first_name

    def get_surname(self, object):
        return object.user.last_name

    get_name.short_description = 'Имя'
    get_surname.short_description = 'Фамилия'


admin.site.register(Profile, ProfileAdmin)