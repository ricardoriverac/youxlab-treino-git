medida1= float(input('digite um valor da primeira reta:'))
medida2=float(input('digite um valor da segunda reta:'))
medida3=float(input('digite um valor da terceira reta:'))

if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1+medida2:
    print('É um triangulo')
if medida2 == medida2 == medida3 :
     print('É um Equilátero')
elif medida1 != medida2 != medida3 != medida1:
    print('É um ESCALENO')
elif medida1 < 90 and medida2 <90 and medida3 <90:
     print('É um ISOSCELES')
else:
    print('Não é um triangulo ')