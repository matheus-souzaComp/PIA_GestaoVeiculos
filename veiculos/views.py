from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Veiculo
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def veiculos(request):
    if request.method == "GET":
        veiculos_list = Veiculo.objects.all()
        return render(request, 'veiculos.html', {'veiculos': veiculos_list})
    elif request.method == "POST":
        modelo = request.POST.get('modelo')
        tag = request.POST.get('tag')
        placa = request.POST.get('placa')
        nSerie = request.POST.get('nSerie')

        veiculo = Veiculo.objects.filter(nSerie=nSerie)

       

        veiculo = Veiculo(
            modelo = modelo,
            tag = tag,
            placa = placa,
            nSerie = nSerie
        )
        veiculo.save()


        #Renderizar template
        return HttpResponse('teste')
    
def att_veiculo(request):
    id_veiculo = request.POST.get('id_veiculo')
    veiculo = Veiculo.objects.filter(id=id_veiculo)
    veiculo_json = json.loads(serializers.serialize('json', veiculo))[0]['fields']
    veiculo_id = json.loads(serializers.serialize('json', veiculo))[0]['pk']
    data = {'veiculo': veiculo_json, 'veiculo_id': veiculo_id}
    return JsonResponse(data)

def update_veiculo(request, id):
    body = json.loads(request.body)

    modelo = body['modelo']
    tag = body['tag']
    placa = body['placa']
    nSerie = body['nSerie']

    veiculo = get_object_or_404(Veiculo, id=id)
    try:
        veiculo.modelo = modelo
        veiculo.tag = tag
        veiculo.placa = placa
        veiculo.nSerie = nSerie
        veiculo.save()
        return JsonResponse({'status': '200', 'modelo': modelo, 'tag': tag, 'placa': placa, 'nSerie': nSerie})
    except:
        return JsonResponse({'status': '500'})