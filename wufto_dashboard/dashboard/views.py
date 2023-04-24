from email import message
from pyexpat import features
from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from numpy import product
import time, datetime
from datetime import datetime, timedelta

from django.shortcuts import redirect, render
from dashboard.forms import Balances_totalesForm, Altcoins_totalesForm,  Estrategia_principal_mensualForm
from .models import Balances_totales, Altcoins_totales,  Estrategia_principal_mensual
from ast import Try
from http import client
from multiprocessing import context
from pydoc import cli
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import TemplateView,ListView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.http import HttpResponse
from requests import request
from django.core.paginator import Paginator
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
#from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django import forms
from usuarios.models import Categoria_Usuario, Usuario
from django.contrib.auth.decorators import permission_required
from usuarios.mixins import ValidarPermisosRequeridosMixin
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql


#Clase para inciar#


@permission_required('dashboard.view_dashboard',login_url='login')
@permission_required('dashboard.add_dashboard',login_url='login')
@permission_required('dashboard.delete_dashboard',login_url='login')
@permission_required('dashboard.change_dashboard',login_url='login')
def ver_balances_totales(request):
        #Balances totales grafico de Datatable 
        cartera_total = search("SELECT `amount_usdt` FROM `balances_totales` WHERE `moneda`='TOTAL_BALANCE' ",)
        cartera_total = cartera_total[0]['amount_usdt']
        cartera_total_dt = float(cartera_total)
        balances_totales_dt = search("SELECT `moneda`, SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales` WHERE NOT `moneda`='TOTAL_BALANCE' GROUP BY `moneda`",)
        query = f"TRUNCATE TABLE wufto.balances_porcentajes;"
        ret = query_(query)
        for balances_total in balances_totales_dt:
             moneda=balances_total['moneda']
             amount_usdt=float(balances_total['amount_usdt'])
             percentage= (amount_usdt * float(100)) / cartera_total_dt
             percentage = truncate(percentage, 2)
             percentage = float(percentage)
             #print(percentage)
             balances_porcentajes=Balances_totales.objects.create(
                    moneda=moneda,
                    percentage=percentage,
                )


        #Balances totales grafico de Altcoins 
        cartera_total = search("SELECT SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales` WHERE NOT `moneda`='TOTAL_BALANCE' AND NOT `moneda`='BTC' AND NOT `moneda`='USDT' AND NOT `moneda`='EUR' AND NOT `moneda`='ETH' ",)
        cartera_total = cartera_total[0]['amount_usdt']
        cartera_total = float(cartera_total)
        balances_totales = search("SELECT `moneda`, SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales` GROUP BY `moneda`",)
        balances_totales_=[]
        for balances_total in balances_totales:
             moneda=balances_total['moneda']
             amount_usdt=float(balances_total['amount_usdt'])
             percentage= (amount_usdt * float(100)) / cartera_total
             percentage = truncate(percentage, 2)
             percentage = float(percentage)
             if moneda != 'TOTAL_BALANCE' and moneda !='ETH' and moneda !='USDT' and moneda !='EUR' and moneda !='BTC':
                balances_totales_.append({
                    'moneda':moneda,
                    'percentage':percentage
                })

        colores = ['#FFF10D' ]
        title='Participacion de Altcoins sobre Total de Altcoins'
        bal = pd.DataFrame(balances_totales_, columns=['moneda','percentage']).set_index(['moneda']).sort_values(by='percentage', ascending=True)
        bal.plot(kind = 'barh', align='center', title=title, xlabel='Porcentaje de participacion', ylabel=' ', color=['#DBBF33'])
        #print(bal)  

        plt.savefig('static/altcoins_totales.png')
        #plt.close()
        plt.clf()

        
        #Balances totales grafico de Balances totales
        
        cartera_total = search("SELECT `amount_usdt` FROM `balances_totales` WHERE `moneda`='TOTAL_BALANCE' ",)
        cartera_total = cartera_total[0]['amount_usdt']
        cartera_total = float(cartera_total)
        altcoins_total = search("SELECT SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales` WHERE NOT `moneda`='TOTAL_BALANCE' AND NOT `moneda`='BTC' AND NOT `moneda`='USDT' AND NOT `moneda`='EUR' AND NOT `moneda`='ETH'",)
        altcoins_total = altcoins_total[0]['amount_usdt']
        altcoins_percentage = (altcoins_total * float(100)) / cartera_total
        altcoins_percentage = truncate(altcoins_percentage, 2)
        altcoins_percentage = float(altcoins_percentage)
        balances_totales__=[]
        balances_totales__.append({
                    'moneda':'ALTCOINS',
                    'percentage':altcoins_percentage
                })
        principal_total = search("SELECT `moneda`, SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales` WHERE `moneda`='BTC' OR `moneda`='USDT' OR `moneda`='EUR' OR `moneda`='ETH' GROUP BY `moneda`",)
        for balance_total in principal_total:
             amount_usdt=float(balance_total['amount_usdt'])
             principal_percentage= (amount_usdt * float(100)) / cartera_total
             principal_percentage = truncate(principal_percentage, 2)
             principal_percentage = float(principal_percentage)
             if principal_percentage >= float(0.01):
                moneda=balance_total['moneda']
                balances_totales__.append({
                        'moneda':moneda,
                        'percentage':principal_percentage
                    })

        #print(balances_totales__)
        bal_ = pd.DataFrame(balances_totales__, columns=['moneda','percentage']).set_index(['moneda'])
        bak__ = bal_.groupby('moneda')['percentage'].sum()
        #a_list = list(range(len(bal_['moneda'])-1))
        a_list = bak__.describe()
        count = int(a_list['count'])
        a_list = list(range(count-1))
        explode = [0.1]
        print("explode")
        for lis in a_list:
            print(a_list)
            element = 0.1
            explode.append(element)
            print(explode)
        colores = ['#DBBF33', '#DBBF60', '#FFD70D', '#FFD97D']
        print(bal_)
        bal_.plot(kind='pie', subplots=True, explode=explode,  autopct='%.2f%%', ylabel=' ', title='Composicion del Fondo Total', colors = colores)
        print(bal_)
        
        plt.savefig('static/balances_totales.png')
        #plt.close()
        plt.clf()
        # % tiempo en un mes de estrategia principal invertida 

        #identifico en que mes estoy 
        time_now = time.time()
        fecha = datetime.utcfromtimestamp(int(time_now)).strftime('%Y-%m-%d')
        ano = fecha[0:4]
        mes = fecha[5:7]
        dias = fecha[8:10]  
        start_time = str(ano) + '-' + str(mes) + '-'
        fechas_dias = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30', '31']
        try:
                dias_a_promediar = search("SELECT COUNT(`fecha`) as 'fecha' FROM `balances_totales_historicos` GROUP BY `fecha`")
                dias_a_promediar = len(dias_a_promediar)

        except:
                 pass

        porcentajes_diarios = []
        for fecha in fechas_dias:
            fecha_ = str(start_time) + str(fecha)
            try:
                cartera_total_estartegia_principal_total = search("SELECT SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales_historicos` WHERE `moneda`='BTC' AND `fecha` = %s OR `moneda`='USDT' AND `fecha` = %s OR `moneda`='EUR' AND `fecha` = %s OR `moneda`='ETH' AND `fecha` = %s ",[fecha_, fecha_, fecha_, fecha_])
                cartera_total_estartegia_principal_total = cartera_total_estartegia_principal_total[0]['amount_usdt']
            except:
                 pass
            try:
                cartera_total_estartegia_principal = search("SELECT `moneda`, SUM(`amount_usdt`) as `amount_usdt` FROM `balances_totales_historicos` WHERE `moneda`='BTC' AND `fecha` = %s OR `moneda`='USDT' AND `fecha` = %s OR `moneda`='EUR' AND `fecha` = %s OR `moneda`='ETH' AND `fecha` = %s GROUP BY `moneda` ",[fecha_, fecha_, fecha_, fecha_])
            except:
                 pass
            for moneda_ in cartera_total_estartegia_principal:
                try:
                    moneda = moneda_['moneda']
                    amount_usdt = float(moneda_['amount_usdt'])
                    percentage_principal = amount_usdt * float(100) / float(cartera_total_estartegia_principal_total)
                    percentage_principal_dias = percentage_principal / int(dias_a_promediar)  
            
                    porcentajes_diarios.append({
                        'moneda':moneda,
                        'percentage_principal_dias':percentage_principal_dias 
                    })
                except:
                     pass
        
        porcentajes_mensuales = pd.DataFrame(porcentajes_diarios, columns=['moneda', 'percentage_principal_dias']).set_index(['moneda'])
        porcentajes_mensuales = porcentajes_mensuales.groupby('moneda')['percentage_principal_dias'].sum()
        a = porcentajes_mensuales.describe()
        count = int(a['count'])
        a_list = list(range(count-1))
        explode = [0.1]
        for lis in a_list:
            element = 0.1
            explode.append(element)
        colores = ['#DBBF33', '#DBBF60', '#FFD70D', '#FFD97D']
        #print(porcentajes_mensuales)
        mes_ = convert(int(mes))
        porcentajes_mensuales.plot(kind='pie', subplots=True, explode=explode, autopct='%.2f%%', ylabel=' ', title=f'Tiempo invertido por moneda durante el mes de {str(mes_)}', colors = colores )
   
        plt.savefig('static/balances_mensual_transcurrido.png')
        #plt.close()
        plt.clf()

        #Altcoins
        take_profit_type = search("SELECT take_profit_type FROM `take_profit_type`",)
        take_profit_type = take_profit_type[0]['take_profit_type']
        if take_profit_type == 'take_profit_bull':
            cartera_total = search("SELECT `balance` FROM `pnl` WHERE `symbol`='TOTAL_ALTCOINS' ",)
            cartera_total = cartera_total[0]['balance']
            cartera_total = float(cartera_total)
            altcoins_totales = search("SELECT * FROM `pnl`",)


            query = f"TRUNCATE TABLE wufto.altcoins_porcentajes;"
            ret = query_(query)

            for altcoins_total in altcoins_totales:
                moneda_alt=altcoins_total['symbol']
                balance_alt=float(altcoins_total['balance'])
                profit_alt=float(altcoins_total['profit_loss_percentage'])
                
                percentage_balance_alt= (balance_alt * 100) / cartera_total
                percentage_profit_alt = truncate(profit_alt, 2)
                altcoins_porcentajes=Altcoins_totales.objects.create(
                        moneda=moneda_alt,
                        percentage_balance=percentage_balance_alt,
                        percentage_profit= percentage_profit_alt
                    )
             
        
        balances_porcentajes=Balances_totales.objects.all()
        altcoins_porcentajes=Altcoins_totales.objects.all()
        return render(request,'dashboard.html', {'balances_porcentajes':balances_porcentajes, 'moneda':moneda, 'percentage':percentage, 'altcoins_porcentajes':altcoins_porcentajes})

#, 'moneda_alt':moneda_alt, 'balance_alt':balance_alt, 'profit_alt':profit_alt, 'percentage_balance':percentage_balance_alt, 'percentage_profit': percentage_profit_alt, 'items_2':items_2






# Auxiliares

def truncate(number: float, max_decimals: int) -> float:
        int_part, dec_part = str(number).split(".")
        return float(".".join((int_part, dec_part[:max_decimals])))

def convert(mes):
     if mes == 1:
        mes = 'ENERO'
     if mes == 2:
        mes = 'FEBRERO'
     if mes == 3:
        mes = 'MARZO'
     if mes == 4:
        mes = 'ABRIL'
     if mes == 5:
        mes = 'MAYO'
     if mes == 6:
        mes = 'JUNIO'
     if mes == 7:
        mes = 'JULIO'
     if mes == 8:
        mes = 'AGOSTO'
     if mes == 9:
        mes = 'SEPTIEMBRE'
     if mes == 10:
        mes = 'OCTUBRE'
     if mes == 11:
        mes = 'NOVIEMBRE'
     if mes == 12:
        mes = 'DICIEMBRE'

     return mes

def search(query:str, variables:list=None):
        results = False
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = '',
                db='wufto'
                )
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(query, variables)
            results = cur.fetchall()
            conn.close()
            print(results)
            return results
        except Exception as e:
            conn.close()
            print('Error retrieving MySQL database record.')
            print(e, True)
            
        return False

def query_(query:str):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = '',
                db='wufto'
                )

            cur = conn.cursor()
            results = cur.execute(query)
            conn.commit()
            conn.close()
            return results

        except Exception as e:
            conn.close()
            print(e)
        
        return False