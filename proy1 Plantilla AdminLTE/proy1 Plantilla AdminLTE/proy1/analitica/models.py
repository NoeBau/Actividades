from django.db import models

class Matricula(models.Model):
    anio = models.IntegerField()
    carrera = models.CharField(max_length=100)
    inscritos = models.IntegerField()
    aprobados = models.IntegerField()
    reprobados = models.IntegerField()

    def __str__(self):
        return f"{self.carrera} - {self.anio}"