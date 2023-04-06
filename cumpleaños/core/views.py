from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms
from core.models import Cumpleañero

def index (request):
    contexto = {
        'titulo':"Bienvenido olvidadizo"
        }
    return render(request, 'core/index.html', contexto)

def acerca_de (request):
    contexto = {
        'titulo':"Acerca de nosotros"
        }
    return render(request, 'core/acerca_de.html', contexto)

def agregar_cumple (request):

    if request.method == "POST":
        form = forms.AgregarCumpleaños(request.POST)
        if form.is_valid():

            cumpleaños_nuevo = Cumpleañero(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                fecha = form.cleaned_data['fecha'],
            )

            cumpleaños_nuevo.save()
            return HttpResponseRedirect (reverse ('cumple_guardado'))
    else:
        form = forms.AgregarCumpleaños()
    contexto = {
        'titulo':"Aquí puede agregar los cumpleaños de sus allegados",
        'form' : form
    }
    return render (request, 'core/agregar_cumple.html', contexto)

def cumple_guardado (request):

    cumpleañeros = Cumpleañero.objects.all()
    contexto = {
        'titulo':"Cumpleaños guardados",
        'cumpleañeros': cumpleañeros,
    }
    return render (request, 'core/cumple_guardado.html', contexto)