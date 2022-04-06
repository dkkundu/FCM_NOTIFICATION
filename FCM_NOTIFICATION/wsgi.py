"""
WSGI config for FCM_NOTIFICATION project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# PYTHON IMPORTS
import os
# DJANGO IMPORTS
from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'FCM_NOTIFICATION.settings'
)

application = get_wsgi_application()
