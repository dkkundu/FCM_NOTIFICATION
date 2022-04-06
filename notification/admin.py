from django.contrib import admin
from .models import FCMSettings


@admin.register(FCMSettings)
class FCMSettingsAdmin(admin.ModelAdmin):
    list_display = ['version', 'is_active', 'api_key']
    list_display_links = ['version', 'is_active', 'api_key']
    search_fields = ['version', 'is_active', 'api_key']
    readonly_fields = [
        'api_key', 'auth_domain', 'database_URL', 'project_id',
        'storage_bucket', 'messaging_sender_id', 'api_key', 'measurement_id', 'server_key', 'action_domain',
        'icon_image'
    ]
