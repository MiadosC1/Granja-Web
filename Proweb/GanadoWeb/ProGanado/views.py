from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("¡Bienvenido a ProGanado! Esta es la página principal.")