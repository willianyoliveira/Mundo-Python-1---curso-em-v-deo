#par ou impar
num = int(input('Digite um número inteiro e vamos descobrir se é par ou impar: '))
resultado = num % 2
if resultado == 1:
    print ('{} é um número ímpar'.format(num))
else:
    print('{} é um número par'.format(num))