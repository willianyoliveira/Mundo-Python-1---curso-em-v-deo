l = float(input('Qual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = (l*h)
tinta = a/2
print('Você vai precisar de {:.2f} litros de tinta para pintar uma parede de {:2f}m²'.format(tinta,a))
