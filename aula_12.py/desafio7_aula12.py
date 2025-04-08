medida1 = float(input('Digite o primeiro número: '))
medida2 = float(input('Digite o segundo número: '))
medida3 = float(input('Digite o terceiro número: '))
if medida1 < medida2+medida3 and medida2 < medida1+medida3 and medida3 < medida1+medida2:
    print('É um triangulo')
if medida1 == medida2 == medida3: 
    print('É um triângulo equilatero')
elif  medida1!= medida2!= medida3!= medida1:
    print('É um triângulo escaleno')
elif medida1 < 90 and medida2 < 90 and medida3 < 90:
    print('Triângulo isosceles')
else:
    print('Não é um triangulo')