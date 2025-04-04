from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.messages import constants
from django .contrib import auth

def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, " 'Senha' e 'Confirmar senha' devem ser iguais")
            return redirect('cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "Senha de possuir 6 ou mais caracteres")
            return redirect('cadastro')
        
        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, constants.ERROR, "O Usuário  informado já existe!")
            return redirect('cadastro')
        
        User.objects.create_user(
            username=usuario, 
            password=senha
        )
        
        return redirect('login')

def login(request): 
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = authenticate(request, username=usuario, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, "Senha inválida")
            return redirect('login')
        
        auth.login(request, user)
        return redirect('mentorados')