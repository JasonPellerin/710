"""
WSGI config for thedabfinder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""


import os, sys
import os.path
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

sys.path.append('/data/vhosts/thedabfinder.com')
os.environ['DJANGO_SETTINGS_MODULE'] = 'thedabfinder.settings'
application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()


