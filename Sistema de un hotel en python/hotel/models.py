from django.core.exceptions import ValidationError
from django.db import models


class TipoHabitacion(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True
    )
    descripcion = models.TextField(
        blank=True
    )
    precio_por_noche = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    capacidad = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = "Tipo de habitación"
        verbose_name_plural = "Tipos de habitación"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    ESTADOS = [
        ("disponible", "Disponible"),
        ("ocupada", "Ocupada"),
        ("reservada", "Reservada"),
        ("limpieza", "Limpieza"),
        ("mantenimiento", "Mantenimiento"),
    ]

    numero = models.CharField(
        max_length=10,
        unique=True
    )
    piso = models.PositiveIntegerField()

    tipo = models.ForeignKey(
        TipoHabitacion,
        on_delete=models.PROTECT,
        related_name="habitaciones"
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="disponible"
    )

    descripcion = models.TextField(
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ["numero"]

    def __str__(self):
        return f"Habitación {self.numero}"


class Cliente(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=150
    )
    telefono = models.CharField(
        max_length=20
    )
    correo = models.EmailField(
        blank=True
    )
    identificacion = models.CharField(
        max_length=50,
        unique=True
    )
    direccion = models.TextField(
        blank=True
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellidos", "nombre"]

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Reservacion(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="reservaciones"
    )

    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.PROTECT,
        related_name="reservaciones"
    )

    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    numero_personas = models.PositiveIntegerField(
        default=1
    )

    anticipo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )

    observaciones = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return (
            f"Reservación de {self.cliente} "
            f"- Habitación {self.habitacion.numero}"
        )

    def clean(self):
        super().clean()

        if self.fecha_entrada and self.fecha_salida:
            if self.fecha_salida <= self.fecha_entrada:
                raise ValidationError(
                    "La fecha de salida debe ser posterior "
                    "a la fecha de entrada."
                )

        if self.habitacion_id and self.numero_personas:
            if self.numero_personas > self.habitacion.tipo.capacidad:
                raise ValidationError(
                    "El número de personas supera la capacidad "
                    "de la habitación."
                )