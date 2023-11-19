from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Motorista
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def motoristas(request):
    if request.method == "GET":
        motoristas_list = Motorista.objects.all()
        return render(request, 'motoristas.html', {'motoristas': motoristas_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        motorista = Motorista.objects.filter(cpf=cpf)

        if motorista.exists():
            #TODO: Adicionar mensagens
            return HttpResponse('motorista já existe')

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            #TODO: Adicionar mensagens
            return HttpResponse('Email inválido')  
        
        #Validar CPF

        motorista = Motorista(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        motorista.save()

        #Renderizar template
        return HttpResponse('teste')
    
    
def att_motorista(request):
    id_motorista = request.POST.get('id_motorista')
    motorista = Motorista.objects.filter(id=id_motorista)
    motorista_json = json.loads(serializers.serialize('json', motorista))[0]['fields']
    motorista_id = json.loads(serializers.serialize('json', motorista))[0]['pk']
    data = {'motorista': motorista_json, 'motorista_id': motorista_id}
    return JsonResponse(data)
   

def update_motorista(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    motorista = get_object_or_404(Motorista, id=id)
    try:
        motorista.nome = nome
        motorista.sobrenome = sobrenome
        motorista.email = email
        motorista.cpf = cpf
        motorista.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})    
