from django.contrib import admin
from .models import FCMSettings


@admin.register(FCMSettings)
class FCMSettingsAdmin(admin.ModelAdmin):
    list_display = ['version', 'is_active', 'api_key']
    list_display_links = ['version', 'is_active', 'api_key']
    search_fields = ['version', 'is_active', 'api_key']
    readonly_fields = ['last_updated']