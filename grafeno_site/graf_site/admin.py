from django.contrib import admin
from .models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'token', 'created_at')
    search_fields = ('ip_address', 'token')
