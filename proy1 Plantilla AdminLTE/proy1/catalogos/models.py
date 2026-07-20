from django.db import models

# Create your models here.
class Carrera(models.Model):
    # Atributos
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField(default=10)

    # Metodos
    def __str__(self):
        return "{0}".format(self.nombre)
    
    def __save__(self):
        self.clave = self.clave.upper()
        self.nombre = self.nombre.upper()
        super(Carrera, self.save())

    class Meta:
        db_table = 'carreras'
        
class Plan(models.Model):
    clave = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50,null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.clave, self.descripcion)

    class Meta:
        verbose_name_plural = "Planes de Estudio"
        db_table = 'planes'
    
class Materia(models.Model):
    clave = models.CharField(max_length=20, help_text="Escribe la clave de la materia")
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField(default=5, null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return "%s ==> %s" % (self.clave, self.nombre)
    
    class Meta:
        db_table = 'materias'


         