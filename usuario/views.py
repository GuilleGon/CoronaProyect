from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse

# Create your views here.


def Registro(request):
	if request.POST:
		post = request.POST
		nuevo_user = Usuario(post['usuario_id'], post['nombre'], post['apellido'], post['nacimiento'], post['email'], post['contrasena'], post['ciudad'], post['codigopostal'])
		nuevo_user.save()
	return render(request, "Registrarse.html")

