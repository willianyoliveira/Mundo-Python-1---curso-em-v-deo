num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
if num3 < num1 > num2:
    print ('{} é o maior número'.format(num1))
if num1 < num2 > num3:
    print ('{} é o maior número'.format(num2))
else: 
    print('{} é o maior número'.format(num3))