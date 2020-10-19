from django.db import models
from django.urls import reverse # se utiliza para redireccionar los path de nuestro proyecto asociado al modelo
import uuid   #se utiliza para relacionar objetos de instancia de libro


# Create your models here.



class Usuario(models.Model):
	"""Model representing an author."""
	rut = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unico dato de personas')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	contraseña = models.CharField(max_length=100)
	recontraseña = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('Usuario-detail', args=[str(self.rut)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'	