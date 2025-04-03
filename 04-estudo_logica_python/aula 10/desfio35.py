medida1= float(input('digite um valor da primeira reta:'))
medida2=float(input('digite um valor da segunda reta:'))
medida3=float(input('digite um valor da terceira reta:'))

if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2:
    print('É um triangulo')
else:
    print('Não é um triangulo')