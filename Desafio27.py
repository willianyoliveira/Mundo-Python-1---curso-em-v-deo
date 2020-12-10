# Faça um programa que leia o nome completo e em seguida morte o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
primnome = (dividido[0])
ultnome = ()
print('Muito prazer!!')
print('Primeiro nome: {}'.format(primnome))
print('Ultimo  nome: {}'.format(dividido[len(dividido)-1]))
