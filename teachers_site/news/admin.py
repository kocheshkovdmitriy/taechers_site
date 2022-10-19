from django.contrib import admin
from .models import New

class NewAdmin(admin.ModelAdmin):
    pass

admin.site.register(New, NewAdmin)


