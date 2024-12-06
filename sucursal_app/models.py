from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=50)
    direccion=models.CharField( max_length=250)
    espacio=models.CharField( max_length=50)
    instrument=models.CharField( max_length=250)
    cantidad=models.IntegerField()
    encargado=models.CharField( max_length=50)
    def __str__(self):
        return self.nombre