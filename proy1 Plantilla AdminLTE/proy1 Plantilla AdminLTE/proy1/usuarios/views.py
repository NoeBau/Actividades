from django.shortcuts import render
from .models import Estudiante
from django.db.models import Count
from datetime import datetime

def dashboard(request):

    total = Estudiante.objects.count()

    activos = Estudiante.objects.filter(estado='activo').count()
    bajas = Estudiante.objects.filter(estado='baja').count()

    # tasa de retención
    retencion = (activos / total * 100) if total > 0 else 0

    # riesgo de deserción
    riesgo = (bajas / total * 100) if total > 0 else 0

    # datos por mes (gráfico)
    datos_mensuales = (
        Estudiante.objects
        .values('fecha_inscripcion__month')
        .annotate(total=Count('id'))
        .order_by('fecha_inscripcion__month')
    )

    meses = []
    valores = []

    for d in datos_mensuales:
        meses.append(d['fecha_inscripcion__month'])
        valores.append(d['total'])

    context = {
        'total': total,
        'retencion': round(retencion, 2),
        'riesgo': round(riesgo, 2),
        'meses': meses,
        'valores': valores
    }

    return render(request, 'dashboard.html', context)