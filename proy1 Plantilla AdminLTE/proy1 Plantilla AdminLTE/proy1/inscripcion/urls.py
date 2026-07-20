from django.urls import path
from inscripcion import views

urlpatterns = [
    path('', views.homeInscripcion, name='homeInscripcion'),

]