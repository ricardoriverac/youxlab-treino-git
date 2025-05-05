medida1 = float(input('Digite a primeira medida: '))
medida2 = float(input('Digite a segunda medida: '))
medida3 = float(input('Digite a terceira medida: '))

if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2:
    print('É um triangulo')
else:
    print('Não é um triangulo')