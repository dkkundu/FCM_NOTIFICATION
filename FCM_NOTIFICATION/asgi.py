"""
ASGI config for FCM_NOTIFICATION project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# PYTHON IMPORTS
import os
# DJANGO IMPORTS
from django.core.asgi import get_asgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'FCM_NOTIFICATION.settings'
)

application = get_asgi_application()
