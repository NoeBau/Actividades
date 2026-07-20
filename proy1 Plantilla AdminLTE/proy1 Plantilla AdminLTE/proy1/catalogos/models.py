from django.db import models


class Carrera(models.Model):
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.clave = self.clave.upper()
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'carreras'


class Plan(models.Model):
    clave = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'planes'


class Materia(models.Model):
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'materias'