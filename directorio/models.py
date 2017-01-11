from django.db import models


class Persona(models.Model):
	num_control = models.IntegerField()
	nombre = models.CharField(max_length=150)
	maquina = models.CharField(max_length=20)
	telefono = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

