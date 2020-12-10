#Calcular Multa
velocidade = float(input('Qual a velocidade do veículo?  '))
if velocidade <= 80:
    print ('{}Km/h, O veículo está dentro do limite de velocidade permitido'.format(velocidade))
else:
    print('{}Km/h, O veículo está acima do limite de velocidade permitido'.format(velocidade))
    multa = (velocidade - 80) * 7
    print ('A multa será de {:.1f} reais'.format(multa))