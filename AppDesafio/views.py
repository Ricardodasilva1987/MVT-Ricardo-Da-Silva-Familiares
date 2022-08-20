from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.
def familiar(request):
    familia = Familia(nombre = "Nara", edad=1, fecha = "2022-09-10" )
    familia.save()
    texto = f" El familiar es de nombre {familia.nombre} tiene {familia.edad} anios y  nacio en {familia.fecha}"
    return HttpResponse(texto)