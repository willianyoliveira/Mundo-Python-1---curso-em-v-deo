import math
an = float(input('Digite o Ângulo que você deseja: '))
sin = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo digitado foi : {}º, O seno é {:.2}, o Coseno é {:.2} e a tangente é {:.2}'.format(an, sin, cos, tan))
