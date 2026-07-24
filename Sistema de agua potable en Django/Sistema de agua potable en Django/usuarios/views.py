from django.db.models import Q
from django.shortcuts import render

from .models import UsuarioServicio


def dashboard(request):
    total_usuarios = UsuarioServicio.objects.count()

    usuarios_activos = UsuarioServicio.objects.filter(
        estado="ACTIVO"
    ).count()

    usuarios_suspendidos = UsuarioServicio.objects.filter(
        estado="SUSPENDIDO"
    ).count()

    usuarios_cancelados = UsuarioServicio.objects.filter(
        estado="CANCELADO"
    ).count()

    contexto = {
        "total_usuarios": total_usuarios,
        "usuarios_activos": usuarios_activos,
        "usuarios_suspendidos": usuarios_suspendidos,
        "usuarios_cancelados": usuarios_cancelados,
    }

    return render(
        request,
        "usuarios/dashboard.html",
        contexto
    )


def lista_usuarios(request):
    busqueda = request.GET.get("buscar", "").strip()

    usuarios = UsuarioServicio.objects.all()

    if busqueda:
        usuarios = usuarios.filter(
            Q(numero_contrato__icontains=busqueda)
            | Q(nombre__icontains=busqueda)
            | Q(direccion__icontains=busqueda)
            | Q(telefono__icontains=busqueda)
        )

    contexto = {
        "usuarios": usuarios,
        "busqueda": busqueda,
    }

    return render(
        request,
        "usuarios/lista_usuarios.html",
        contexto
    )