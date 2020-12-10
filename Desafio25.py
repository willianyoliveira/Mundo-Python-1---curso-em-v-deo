# Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não "Silva" no nome
nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Você tem Silva no nome? {}'.format('SILVA' in nome))