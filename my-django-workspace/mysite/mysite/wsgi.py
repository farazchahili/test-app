import os
import sys

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'wsgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()