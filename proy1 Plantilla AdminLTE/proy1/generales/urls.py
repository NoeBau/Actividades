from django.urls import path 

from generales import views

urlpatterns = [
    path('home/', views.index, name='index'),
]
