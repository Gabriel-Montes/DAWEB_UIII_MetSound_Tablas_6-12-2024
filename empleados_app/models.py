from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_emple=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=150)
    puesto=models.CharField( max_length=50)
    sueldo=models.FloatField()
    edad=models.IntegerField()
    direccion=models.CharField( max_length=250)
    celular=models.IntegerField()
    def __str__(self):
        return self.nombre