# coding: utf-8
from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'cpf', 'email', 'university',  'course', 'kind', 'created_at'
    )
    list_filter = ('kind', 'is_active')
    search_fields = ['name', 'cpf', 'email']

    class Media:
        js = ('js/jquery.maskedinput.js', 'js/person.js')


admin.site.register(Person, PersonAdmin)
