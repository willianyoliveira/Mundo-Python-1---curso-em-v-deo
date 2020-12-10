print('PARABENS, VOCE RECEBER 5% DE DESCONTO')
valor = float(input('Digite o preço do produto e vamos calcular o novo valor com o desconto:'))
desconto = valor * (5/100)
novovalor = valor - desconto
print ('Com o desconto de 5% o produto passa a custar : {:.2f}'.format(novovalor))
