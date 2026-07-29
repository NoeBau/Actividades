from django.shortcuts import render

from .models import Cliente, Habitacion, Reservacion


def inicio(request):
    total_habitaciones = Habitacion.objects.count()

    habitaciones_disponibles = Habitacion.objects.filter(
        estado="disponible",
        activa=True
    ).count()

    habitaciones_ocupadas = Habitacion.objects.filter(
        estado="ocupada",
        activa=True
    ).count()

    total_clientes = Cliente.objects.count()

    total_reservaciones = Reservacion.objects.count()

    reservaciones_recientes = Reservacion.objects.select_related(
        "cliente",
        "habitacion"
    ).order_by("-fecha_creacion")[:5]

    contexto = {
        "total_habitaciones": total_habitaciones,
        "habitaciones_disponibles": habitaciones_disponibles,
        "habitaciones_ocupadas": habitaciones_ocupadas,
        "total_clientes": total_clientes,
        "total_reservaciones": total_reservaciones,
        "reservaciones_recientes": reservaciones_recientes,
    }

    return render(
        request,
        "hotel/inicio.html",
        contexto
    )