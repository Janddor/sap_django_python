from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    # return HttpResponse('Hola mundo desde Django'.center(60, "*"))
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id') # por defecto ascendente, '-id' descendente
    return render(request, 'bienvenido.html',{'no_personas':no_personas, 'personas':personas})
