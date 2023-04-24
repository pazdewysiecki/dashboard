from http.client import ImproperConnectionState
from django.contrib import admin
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

from usuarios.models import Usuario
from .models import Balances_totales, Altcoins_totales,  Estrategia_principal_mensual
# Register your models here.


    

admin.site.register ([Balances_totales, Altcoins_totales,  Estrategia_principal_mensual])
#admin.site.register(Product, ProductAdmin)