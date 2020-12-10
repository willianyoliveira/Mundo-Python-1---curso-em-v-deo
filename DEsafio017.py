'''Catetos  e hipotenusa'''
import math
'''x = float(input('Qual o comprimento do cateto oposto: '))
y = float(input('Qual o comprimento do cateto adjascente: '))
h = (x*x + y*y)**0.5
print('O valor da hipotenusa é {.2f}.'.format(h))'''

x = float(input('Qual o comprimento do cateto oposto: '))
y = float(input('Qual o comprimento do cateto adjascente: '))
h = math.hypot(x,y)
print('O valor da hipotenusa é {:.2f}.'.format(h))