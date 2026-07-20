from django.shortcuts import render

# Create your views here.
def homeInscripcion(request):
    return render(request, 'homeInscripcion.html')

