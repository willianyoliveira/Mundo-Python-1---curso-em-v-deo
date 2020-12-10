# ler uma frase, quantas vezes aparece a ltra a, em q posição ela aparece na primeira vez, em que posição aparece na ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "a" apartece {} vezes'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A ultima letra "A", apareceu na posição {}'.format(frase.rfind('A')+1))
# rfind é usado para procurar a aprtir do lado direito, consequentemente ele mostrará a ultima
