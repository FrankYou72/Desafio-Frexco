from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['register_date']}),
        ('Personal data', {'fields' : ['name', 'email', 'cpf']})
    ]

    list_display = ['name', 'email', 'cpf', 'register_date']
    search_fields = ['name']

admin.site.register(Client, ClientAdmin)
# Register your models here.
