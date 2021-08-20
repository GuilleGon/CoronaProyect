from django.http import HttpResponse
from django.shortcuts import render
from usuario.models import Usuario
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def inicio(request):
	return render(request, "index.html")

def AutoTest(request):
	return render(request, "AutoTest.html")

def Arreglando(request):
	return render(request, "Arreglando.html")

def Cuidados(request):
	return render(request, "Cuidados.html")

def Login(request):
	return render(request, "login.html")

def Adolescente(request):
	return render(request, "Adolescente.html")

def Home(request):
	user = Usuario.objects.all()
	respuesta_string = '<br/>'.join(["id: %s"% (user.usuario_id(1)) ])
	return HttpResponse(respuesta_string)

def jogos(request):
	return render(request, "ado_juegos.html")

def gym(request):
	return render(request, "ado_gym.html")

def music(request):
	return render(request, "ado_musica.html")