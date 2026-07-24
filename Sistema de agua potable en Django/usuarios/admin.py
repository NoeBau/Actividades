from django.contrib import admin

from .models import UsuarioServicio


@admin.register(UsuarioServicio)
class UsuarioServicioAdmin(admin.ModelAdmin):

    list_display = (
        "numero_contrato",
        "nombre",
        "tipo_servicio",
        "estado",
        "telefono",
        "fecha_alta",
    )

    search_fields = (
        "numero_contrato",
        "nombre",
        "direccion",
        "telefono",
    )

    list_filter = (
        "tipo_servicio",
        "estado",
        "fecha_alta",
    )

    ordering = (
        "nombre",
    )