from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cidade', 'data_cadastro')
    search_fields = ('nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome', 'cidade')
    readonly_fields = ('data_cadastro',)
    ordering = ('nome', 'sobrenome')
