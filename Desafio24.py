# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "santo"
city = str(input('Digite o nome da sua cidade: ')).strip()
print(city[:5].upper() == 'SANTO')


# nome = city.split()
# nomecity = (nome[0])
# if nomecity == 'Santo':
#    print('Legal, o primeiro nome é Santo')
# if nomecity == 'santo':
#   print('Legal, o primeiro nome é Santo')
# else:
#    print('O nome da cidade é {}, nada demais'.format(city))