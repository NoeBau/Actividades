from django.urls import path

from . import views


app_name = "usuarios"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("usuarios/", views.lista_usuarios, name="lista_usuarios"),
]