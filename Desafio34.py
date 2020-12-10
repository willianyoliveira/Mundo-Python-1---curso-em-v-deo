#aumentos multiplos
sal = float(input('Digite seu salário atual: '))
if sal >= 1250 :
    salnovo = sal + (sal * 0.10)
    print('Seu salário novo será {} reais'.format(salnovo))
else: 
    salnovo = sal + (sal*0.15)
    print('Seu salário novo será {} reais'.format(salnovo))
