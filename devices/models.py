from django.db import models

# Create your models here.
# crear un modelos para los dispositivos que se van a registrar en la base de datos con las variables equipos, marca y modelo con el que se pueda hacer un CRUD
class Device(models.Model):
    equipos = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return self.equipos