from django.db import models

# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=80)

    def __str__(self):
        return self.materia

class Tipo_juicio(models.Model):
    tipo_juicio = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo_juicio

class Tipo_resolucion(models.Model):
    tipo_resolucion = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo_resolucion

class Estatus(models.Model):
    estatus = models.CharField(max_length=80)

    def __str__(self):
        return self.estatus

class Ubicacion(models.Model):
     ubicacion = models.CharField(max_length=80)
     
     def __str__(self):
         return self.ubicacion

class Municipio(models.Model):
    municipio = models.CharField(max_length=90)
    
    def __str__(self):
        return self.municipio

class Poblacion(models.Model):
    poblacion = models.CharField(max_length=70)
    municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.poblacion

class Juzgado(models.Model):
    nombre_juzgado = models.CharField(max_length=70)
    encargado = models.CharField(max_length=70)
    telefono = models.CharField(max_length=30)
    poblacion = models.ForeignKey(Poblacion, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_juzgado

class Juez(models.Model):
    nombre_juez = models.CharField(max_length=80)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    validado_juez = models.BooleanField(default=False)
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_servidor
           
class Expediente(models.Model):
    num = models.IntegerField()
    agno = models.DateField()
    fecha_turno = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, null=False, blank=False, on_delete=models.CASCADE)
    fecha_firma = models.DateField()
    observaciones = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    servidor = models.ForeignKey(Servidor, null=True, blank=True, on_delete=models.CASCADE)
    tipo_juicio = models.ForeignKey(Tipo_juicio, null=True, blank=True, on_delete=models.CASCADE)
    tipo_resolucion = models.ForeignKey(Tipo_resolucion, null=True, blank=True, on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus, null=True, blank=True, on_delete=models.CASCADE)
    juzgado = models.ForeignKey(Juzgado,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} / {1}'.format(self.num, self.agno)
