
import imp
from django import forms
from .models import Balances_totales, Altcoins_totales,  Estrategia_principal_mensual



class Balances_totalesForm(forms.ModelForm):
    class Meta:
        model = Balances_totales
        fields = ['moneda', 'percentage']
        labels = {
                'moneda': "Moneda:",
                'percentage': "Participacion sobre total:",
            }
        
class Altcoins_totalesForm(forms.ModelForm):
    class Meta:
        model = Altcoins_totales
        fields = ['moneda', 'percentage_balance', 'percentage_profit']
        labels = {
                'moneda': "Moneda:",
                'percentage_balance': "Porcentaje del Balance sobre el total:",
                'percentage_profit': "Porcentaje del rendimiento:"
            }
        
class Estrategia_principal_mensualForm(forms.ModelForm):
    class Meta:
        model = Estrategia_principal_mensual
        fields = ['moneda', 'porcentaje_tiempo_invertido']
        labels = {
                'moneda': "Moneda:",
                'porcentaje_tiempo_invertido': "Porcentaje del Tiempo invertido mensual:",
            }

