from django.contrib import admin

from .models import regis


class regAdmin(admin.ModelAdmin):
    list_display = ('appointment_opt','cl','sp','stat')

admin.site.register(regis,regAdmin)
