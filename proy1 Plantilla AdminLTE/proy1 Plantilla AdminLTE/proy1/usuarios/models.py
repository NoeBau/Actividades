from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    semestre = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('baja', 'Baja'),
        ('egresado', 'Egresado')
    ])
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return self.nombre