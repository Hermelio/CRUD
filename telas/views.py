from django.shortcuts import render, redirect
from .models import Cliente


def home(request):
    template_name = 'crud/home.html'
    user = Cliente.objects.all()
    contexto = {"user":user}
    return render(request, template_name, contexto)

def cadastro(request):
    template_name = 'crud/cadastro.html'

    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        cpf = request.POST['cpf']
        status = request.POST['status']
        status_code = False
        if status == 'Ativo':
            status = True
        if Cliente.objects.filter(email=email).exists():
            print("Cliente ja cadastrado")
            
        else:
            Cliente.objects.create(nome=nome, email=email, telefone=telefone, cpf= cpf, status = status_code)
            return redirect('telas:home')

    return render(request, template_name)


def new_user_ajax(request):
    ...
