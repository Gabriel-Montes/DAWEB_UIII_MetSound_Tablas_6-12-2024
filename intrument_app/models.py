from django.db import models

# Create your models here.

class Instrument(models.Model):
    id_instru=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=50)
    tamano=models.CharField( max_length=50)
    estado=models.CharField( max_length=50)
    lugar=models.CharField( max_length=50)
    mantenimiento=models.CharField(max_length=50)
    vendido=models.CharField( max_length=2)
    def __str__(self):
        return self.id_instru