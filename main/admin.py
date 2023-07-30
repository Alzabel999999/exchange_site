from django.contrib import admin, messages
from .models import RequestExchange

# Register your models here.
@admin.register(RequestExchange)
class RequestExchangeAdmin(admin.ModelAdmin):
    list_display = ['fio', 'telegram_login', 'input', 'amount_input', 'output', 'amount_output']
    list_display_links = ('fio', )
    readonly_fields = []
