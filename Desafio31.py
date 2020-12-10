#Preço da passagem
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da passagem será {:.2f} reais'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O valor da passagem será {:.2f} reais'.format(passagem))