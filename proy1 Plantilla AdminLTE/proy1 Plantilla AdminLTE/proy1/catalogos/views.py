from django.shortcuts import render
from .models import Carrera, Plan, Materia

def dashboard(request):
    return render(request, 'home.html')

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')


def carrerasListas(request):
    carreras = Carrera.objects.all()
    datos = {'carreras': carreras}
    return render(request, 'carrerasListar.html', datos)