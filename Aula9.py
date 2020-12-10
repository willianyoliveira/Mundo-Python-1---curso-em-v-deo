# O primeiro número indica por onde ele vai começar mostrar
# O segundo número é indica até onde ele vai mostrar
# O terceiro número indica o salto que será dado, ex: de 2 em 2
# Para escrever um texto longo, não precisa dar print em cada linha. Basta utilizar aspas triplas (''')

frase = 'prova de python!'
#
print(frase[1:12:])

# para contar quantas vezes determinada letra se repete em uma frase
print(frase.count('o'))

# Posso utilizar a combinação abaixo para que o python passe a contar as letras maiúsculas e minúsculas.
print(frase.upper().count('O')) # Quantidade de 'o' dentro da frase que foi jogada para letra maiúscula
# Utilizar lower para minúsculo

#PAra contar a quantidade de letras
print(len(frase))

#Retira os espações indesejados, antes e edepois da frase
print(len(frase.strip()))

# Trocar uma coisa pela outra
print(frase.replace('python', 'android'))

print(frase.split()) # criou uma lista

# Imprimir apenas a posição indicada
dividivo = (frase.split())
print(dividivo[1])
