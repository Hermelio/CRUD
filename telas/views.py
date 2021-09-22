from django.shortcuts import render
from .models import Cliente


def home(request):
    template_name = 'crud/home.html'
    user = Cliente.objects.all()
    contexto = {"user":user}
    return render(request, template_name, contexto)

def cadastro(request):
    template_name = 'crud/cadastro.html'
    return render(request, template_name)
