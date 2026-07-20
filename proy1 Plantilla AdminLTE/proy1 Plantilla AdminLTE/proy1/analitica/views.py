from django.shortcuts import render
from .models import Matricula

def dashboard(request):
    return render(request, 'dashboard.html')

def indicadores(request):
    return render(request, 'dashboard.html')

def estudiantes(request):
    return render(request, 'dashboard.html')

def desercion(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'home.html')