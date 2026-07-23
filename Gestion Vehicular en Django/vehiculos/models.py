from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class Vehiculo(models.Model):
    marca = models.CharField(
        max_length=50,
        verbose_name="Marca"
    )

    modelo = models.CharField(
        max_length=50,
        verbose_name="Modelo"
    )

    anio = models.PositiveIntegerField(
        verbose_name="Año",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(date.today().year + 1),
        ],
    )

    placa = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Placa"
    )

    color = models.CharField(
        max_length=30,
        verbose_name="Color"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Vehículo activo"
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro"
    )

    class Meta:
        ordering = ["-fecha_registro"]
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"


class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name="mantenimientos"
    )

    tipo = models.CharField(
        max_length=50,
        verbose_name="Tipo de mantenimiento"
    )

    fecha = models.DateField(
        verbose_name="Fecha"
    )

    costo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Costo"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Mantenimiento"
        verbose_name_plural = "Mantenimientos"

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.tipo}"