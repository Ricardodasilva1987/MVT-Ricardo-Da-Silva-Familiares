from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from datetime import datetime
from multiprocessing import context
from pipes import Template
from django.template import Context,Template,loader

# Create your views here.
def familiar(request):

    
    familia1 = Familia(nombre = "Nara", edad=1, fecha = "2022-09-11" )
    familia1.save()
    familia2 = Familia(nombre = "Paula", edad=18, fecha = "1999-09-10" )
    familia2.save()
    familia3 = Familia(nombre = "Ricardo", edad=35, fecha = "2022-09-10" )
    familia3.save()
    #texto = f" El familiar es de nombre {familia.nombre} tiene {familia.edad} anios y  nacio en {familia.fecha}"
    #diccionario = {"nombre":familia1.nombre, "edad":familia1.edad, "fecha":familia1.fecha}
    lista =[familia1,familia2,familia3]
    diccionario = {"lista":lista}
    plantilla = loader.get_template("template.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


def familia1 (request):
    return HttpResponse(f"")








