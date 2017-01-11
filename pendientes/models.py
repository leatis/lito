from django.db import models
from directorio.models import Persona

class Pendiente(models.Model):
	descripcion = models.CharField(max_length=200)
	fecha_inicio = models.DateTimeField('Fecha de inicio')
	estado = models.CharField(max_length=9)
	elaboro = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Accion(models.Model):
	descripcion = models.CharField(max_length=200)
	pendiente = models.ForeignKey(Pendiente, on_delete=models.CASCADE)
	fecha_accion = models.DateTimeField('Realizada el')
	realizo = models.ForeignKey(Persona, on_delete=models.CASCADE)
	
