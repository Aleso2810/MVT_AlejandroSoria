from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
from django.template import loader

def familiar(request):
    familiar=Familiar(primer_nombre="Noah", segundo_nombre="Cristofer", primer_apellido="Soria",
    segundo_apellido="Gaon", fecha_nacimiento="2016-05-24", numero_favorito=4, parentezco="Hijo")
    familiar.save()
    texto= f"Familiar Creado: {familiar.primer_nombre} {familiar.primer_apellido} Parentezco: {familiar.parentezco}"
    return HttpResponse(texto)

def home (request):
    nombre="Alejandro"
    apellido="Soria"
    diccionario={"nombre":nombre,"apellido":apellido}
    
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)