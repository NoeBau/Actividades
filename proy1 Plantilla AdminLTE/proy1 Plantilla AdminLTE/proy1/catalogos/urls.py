from django.urls import path
from catalogos import views

urlpatterns = [
    path('', views.homeCatalogos, name='homeCatalogos'),
    path('carreras/listar/', views.carrerasListas, name='carreraListas'),
    path('', views.homeCatalogos, name='homeCatalogos'),
]