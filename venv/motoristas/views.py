from django.shortcuts import render
from django.http import HttpResponse
from .models import motorista, carros

def motorista(request):
    if request.method == "GET":
        return render(request, 'motorista.html')
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

        motorista = motorista.objects.filter(codigo=codigo)

        if motorista.exists():
            return HttpResponse('Motorista já existe')
        
        motorista = motorista(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            telefone = telefone,
            codigo = codigo,
        )
        motorista.save()

        for carros, placa, ano, kmdeoleo in zip(carros, placa, ano,kmdeoleo):
            carros = carros(carro=carros, placa=placa, ano=ano, motorista=motorista, kmdeoleo=kmdeoleo)
            carros.save()
        return HttpResponse('Cadastro realizado com sucesso')
    
    return render(request, 'motoristas.html')