from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.IntegerField(primary_key=True) 
    cantidad=models.IntegerField()
    instrument=models.CharField( max_length=50)
    precio_tot=models.FloatField()
    id_cliente=models.IntegerField()
    id_sucursal=models.IntegerField()
    id_empleado=models.IntegerField()
    def __str__(self):
        return self.id_venta