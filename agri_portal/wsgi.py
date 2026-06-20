"""
WSGI config for agri_portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_portal.settings')

application = get_wsgi_application()
app = application

# Automatically run database migrations on server boot
try:
    print("Executing automatic database migrations on startup...")
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Automatic migration check failed: {e}")
