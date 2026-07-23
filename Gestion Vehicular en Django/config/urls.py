from django.contrib import admin
from django.urls import path
from vehiculos import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("vehiculos/", views.lista, name="lista"),
    path("vehiculos/nuevo/", views.crear, name="crear"),
    path("vehiculos/editar/<int:id>/", views.editar, name="editar"),
    path("vehiculos/eliminar/<int:id>/", views.eliminar, name="eliminar"),
]