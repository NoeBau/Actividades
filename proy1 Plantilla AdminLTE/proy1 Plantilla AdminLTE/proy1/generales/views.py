from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'home.html') 

    
    #return HttpResponse('<h3>Pagina principal del sistema</h3>')

def home(request):
    return HttpResponse('<h1>Estas en el Home del sistema ... </h1>')

    '''
    data = {
        'numero':1,
        'nombre':'Alicia',
        'edad':20
    }
    return JsonResponse(data)
    '''
