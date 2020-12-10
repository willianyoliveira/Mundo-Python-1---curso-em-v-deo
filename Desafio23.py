# faça um programa que leia um número de 1 ate 9999 e mostre quantas unidades, centenas, e dezenas possui
num = int(input('Digite um número de 1 a 9999 e iremos decompor: '))
u = num//1 %10
d = num//10 %10
c = num//100 %10
m = num//1000 %10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))