from django.shortcuts import render
from django.http import HttpResponse
from .models import Motorista

def Motorista(request):
    if request.method == "GET":
        return render(request, 'motoristas.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        codigo = request.POST.get('codigo')
        carros = request.POST.getlist ('carros')
        placa = request.POST.getlist ('placa')
        ano = request.POST.getlist ('ano')
        kmdeoleo = request.POST.getlist ('kmdeoleo')

        motoristas = motoristas.objects.filter(codigo=codigo)

        if motoristas.exists():
            return HttpResponse('motorista já existe')
        
        motoristas = motoristas(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            telefone = telefone,
            codigo = codigo,
        )
        motoristas.save()

        for carros, placa, ano, kmdeoleo in zip(carros, placa, ano,kmdeoleo):
            carros = carros(carro=carros, placa=placa, ano=ano, motoristas=motoristas, kmdeoleo=kmdeoleo)
            carros.save()
        return HttpResponse('Cadastro realizado com sucesso')
    
    return render(request, 'motoristas.html')