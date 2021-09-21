from django.shortcuts import render

def home(request):
    template_name = 'crud/home.html'
    return render(request, template_name)

def cadastro(request):
    template_name = 'crud/cadastro.html'
    return render(request, template_name)
