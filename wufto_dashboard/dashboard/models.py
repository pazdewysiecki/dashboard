from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from django.db import models
from matplotlib import image
from matplotlib.style import available
from usuarios.models import Categoria_Usuario, Usuario
from django.utils.safestring import mark_safe


# Create your models here.


class Balances_totales(models.Model):
    moneda = models.CharField(max_length=300, primary_key= True)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.moneda

    class Meta:
        db_table = 'balances_porcentajes'
        verbose_name = 'Balances_porcentajes'
        verbose_name_plural = 'Balances_porcentajes'
        ordering = ['percentage']

class Altcoins_totales(models.Model):
    moneda = models.CharField(max_length=300, primary_key= True)
    percentage_balance = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_profit = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.moneda

    class Meta:
        db_table = 'altcoins_porcentajes'
        verbose_name = 'Altcoins_porcentajes'
        verbose_name_plural = 'Altcoins_porcentajes'
        ordering = ['percentage_balance']

     

class Estrategia_principal_mensual(models.Model):
    moneda = models.CharField(max_length=300, primary_key= True)
    porcentaje_tiempo_invertido = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.moneda

    class Meta:
        db_table = 'estrategia_principal_mensual'
        verbose_name = 'Estrategia_principal_mensual'
        verbose_name_plural = 'Estrategia_principal_mensual'
        ordering = ['porcentaje_tiempo_invertido']


