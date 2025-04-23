#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


largura = float(input('Digite a largura de um terreno retangular: (m) '))
comprimento = float(input('Digite o comprimento de um terreno retangular: (m) '))

def area(a,  b):
    areaTotal = a * b
    print(f'A área total de um retângulo {a}x{b} é {areaTotal}m²')
area(largura, comprimento)