a = float(input('Digite o valor  da primeira reta: '))
b = float(input('Digite o valor  da segunda reta: '))
c = float(input('Digite o valor  da terceira reta: '))
if a>=b+c or b>=a+c or c>=b+a or a<=0 or b<=0 or c<=0 :
    print ('As retas não podem formar um triangulo')
else: 
    print('as retas podem formar um triangulo')
