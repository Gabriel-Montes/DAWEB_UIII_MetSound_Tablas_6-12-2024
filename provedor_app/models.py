from django.db import models

# Create your models here.

class Provedor(models.Model):
    id_prove=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=50)
    cantidad=models.IntegerField()
    fecha_entre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    estado=models.CharField( max_length=50)
    instrument=models.CharField( max_length=50)
    def __str__(self):
        return self.nombre