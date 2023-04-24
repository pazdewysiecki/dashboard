from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from .views import ver_balances_totales

app_name='dasboard'


urlpatterns = [
    path('dashboard/', login_required(ver_balances_totales), name = 'dashboard'),

    ]

