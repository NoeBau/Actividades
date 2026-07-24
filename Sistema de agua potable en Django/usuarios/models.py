from django.db import models


class UsuarioServicio(models.Model):

    TIPO_SERVICIO = [
        ("DOMESTICO", "Doméstico"),
        ("COMERCIAL", "Comercial"),
        ("INDUSTRIAL", "Industrial"),
        ("PUBLICO", "Público"),
    ]

    ESTADO = [
        ("ACTIVO", "Activo"),
        ("SUSPENDIDO", "Suspendido"),
        ("CANCELADO", "Cancelado"),
    ]

    numero_contrato = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de contrato"
    )

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre completo"
    )

    direccion = models.CharField(
        max_length=250
    )

    telefono = models.CharField(
        max_length=15,
        blank=True
    )

    correo = models.EmailField(
        blank=True
    )

    tipo_servicio = models.CharField(
        max_length=20,
        choices=TIPO_SERVICIO,
        default="DOMESTICO"
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADO,
        default="ACTIVO"
    )

    fecha_alta = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.numero_contrato} - {self.nombre}"

    class Meta:
        verbose_name = "Usuario del Servicio"
        verbose_name_plural = "Usuarios del Servicio"
        ordering = ["nombre"]