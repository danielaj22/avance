from django.db import models

class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=50)
    horario=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre
