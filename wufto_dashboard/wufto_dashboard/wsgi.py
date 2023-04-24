"""
WSGI config for wufto_dashboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wufto_dashboard.settings.local') #local o produccion

#para local:
application = get_wsgi_application()


#para producción:

#application = Cling(get_wsgi_application())



#application = DjangoWhiteNoise(application)