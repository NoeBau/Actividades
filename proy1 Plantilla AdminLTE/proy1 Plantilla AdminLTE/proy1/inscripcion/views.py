from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def indicadores(request):
    return render(request, 'indicadores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def desercion(request):
    return render(request, 'desercion.html')