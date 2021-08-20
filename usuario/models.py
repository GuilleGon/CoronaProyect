from django.db import models

# Create your models here.

class Usuario(models.Model):
	usuario_id = models.IntegerField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	nacimiento = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	contrasena = models.CharField(max_length=20)
	ciudad = models.CharField(max_length=100)
	codigopostal = models.CharField(max_length=6)