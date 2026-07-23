from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VehiculoForm
from .models import Vehiculo


def dashboard(request):
    total = Vehiculo.objects.count()
    activos = Vehiculo.objects.filter(activo=True).count()
    inactivos = Vehiculo.objects.filter(activo=False).count()

    vehiculos_recientes = Vehiculo.objects.order_by(
        "-fecha_registro"
    )[:5]

    context = {
        "total": total,
        "activos": activos,
        "inactivos": inactivos,
        "vehiculos_recientes": vehiculos_recientes,
    }

    return render(request, "dashboard.html", context)


def lista(request):
    consulta = request.GET.get("q", "").strip()

    vehiculos = Vehiculo.objects.all()

    if consulta:
        vehiculos = vehiculos.filter(
            Q(marca__icontains=consulta)
            | Q(modelo__icontains=consulta)
            | Q(placa__icontains=consulta)
            | Q(color__icontains=consulta)
        )

    paginador = Paginator(vehiculos, 5)
    numero_pagina = request.GET.get("page")
    pagina = paginador.get_page(numero_pagina)

    context = {
        "vehiculos": pagina,
        "consulta": consulta,
    }

    return render(request, "lista.html", context)


def crear(request):
    if request.method == "POST":
        formulario = VehiculoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(
                request,
                "El vehículo se registró correctamente."
            )
            return redirect("lista")
    else:
        formulario = VehiculoForm()

    return render(
        request,
        "form.html",
        {
            "form": formulario,
            "titulo": "Registrar vehículo",
            "texto_boton": "Guardar vehículo",
        },
    )


def editar(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == "POST":
        formulario = VehiculoForm(
            request.POST,
            instance=vehiculo
        )

        if formulario.is_valid():
            formulario.save()
            messages.success(
                request,
                "El vehículo se actualizó correctamente."
            )
            return redirect("lista")
    else:
        formulario = VehiculoForm(instance=vehiculo)

    return render(
        request,
        "form.html",
        {
            "form": formulario,
            "titulo": "Editar vehículo",
            "texto_boton": "Actualizar vehículo",
        },
    )


def eliminar(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == "POST":
        vehiculo.delete()

        messages.success(
            request,
            "El vehículo se eliminó correctamente."
        )

        return redirect("lista")

    return render(
        request,
        "confirmar_eliminar.html",
        {"vehiculo": vehiculo},
    )