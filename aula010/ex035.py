lado1= int(input('Tamanho do primeiro lado: '))
lado2=int(input('Tamanho do segundo lado: '))
lado3=int(input('Tamanho do terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print('Não e um triângulo ')
else:
    print('E um  triângulo ')

