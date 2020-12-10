# Nome completo
nome = str(input('Digite seu nome completo: ')).strip()
# strip é usado para que não seja considerado os espaços que o usuário venha a colocar entes e depois no nome

# Nome em maiúsculo
print('nome todo escrito em maiúsculo: {} '.format((nome.upper())))
# Nome tode em minúsculo
print('nome todo escrito em minúsculo: {} '.format((nome.lower())))
# Quantas letras tem o nome tem (sem considerar os espaços)
print('Quantas letras tem o nome tem (sem considerar os espaços antes e depois do nome): {}'.format(len(nome) - nome.count(' ')))
# Quantas letras tem o primeiro nome
dividido = nome.split()
primnome = (dividido[0])
print('O primeiro nome possui: {} letras'.format((len(primnome))))