"""
URL configuration for wufto_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.decorators import login_required
from dashboard.views import ver_balances_totales
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import Login



urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('usuarios/',include(('usuarios.urls', 'usuarios'))),
    path('dashboard/',include(('dashboard.urls','dashboard'))),
    path('',login_required(ver_balances_totales), name = 'dashboard'),
    path('accounts/login/', Login.as_view(),{'template_name':'login.html'}, name = 'login'),
    path ('logout/', logout_then_login, name = 'logout')
    ]
