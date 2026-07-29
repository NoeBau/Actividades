from django.contrib import admin

from .models import (
    Cliente,
    Habitacion,
    Reservacion,
    TipoHabitacion,
)


@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio_por_noche",
        "capacidad",
    )

    search_fields = (
        "nombre",
    )


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "piso",
        "tipo",
        "estado",
        "activa",
    )

    list_filter = (
        "estado",
        "piso",
        "tipo",
        "activa",
    )

    search_fields = (
        "numero",
        "tipo__nombre",
    )

    list_editable = (
        "estado",
        "activa",
    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellidos",
        "identificacion",
        "telefono",
        "correo",
    )

    search_fields = (
        "nombre",
        "apellidos",
        "identificacion",
        "telefono",
    )


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "habitacion",
        "fecha_entrada",
        "fecha_salida",
        "estado",
        "anticipo",
    )

    list_filter = (
        "estado",
        "fecha_entrada",
        "fecha_salida",
    )

    search_fields = (
        "cliente__nombre",
        "cliente__apellidos",
        "habitacion__numero",
    )

    date_hierarchy = "fecha_entrada"