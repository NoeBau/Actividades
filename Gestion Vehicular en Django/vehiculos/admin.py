from django.contrib import admin

from .models import Mantenimiento, Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        "placa",
        "marca",
        "modelo",
        "anio",
        "color",
        "activo",
        "fecha_registro",
    )

    search_fields = (
        "placa",
        "marca",
        "modelo",
    )

    list_filter = (
        "activo",
        "marca",
        "anio",
    )

    ordering = (
        "-fecha_registro",
    )


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = (
        "vehiculo",
        "tipo",
        "fecha",
        "costo",
    )

    search_fields = (
        "vehiculo__placa",
        "vehiculo__marca",
        "tipo",
    )

    list_filter = (
        "tipo",
        "fecha",
    )