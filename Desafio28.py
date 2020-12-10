from random import randint
print('VocÊ consegue advinhar o número que eu estou pensando?')
num = int(input('Escolha um número entre 0 e 5: '))
computador = randint(0,5)
if num == computador:
    print ('nós pensamos no mesmo número!')
else:
    print('Eu pensei no número {} e você pensou em {}'.format(computador, num))