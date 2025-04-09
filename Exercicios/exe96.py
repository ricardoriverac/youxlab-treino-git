#Faça um programa que tenha uma função chamada area(), que recebe dimensoes de um terreno
#retangular (largura e comprimento) e mostre a aŕea do terreno

def lin():
    print("-=-" * 15)

def cabecalho(texto):
    lin()
    print(texto.center(2))
    lin()

cabecalho("Programa de calcular área de um terreno.")

def area(largura, comprimento):
    calculo = comprimento * largura
    print(f"A área de um terreno {largura} x {comprimento} é de {calculo} m².")


comprimento = float(input("\nDigite um comprimento: "))
largura = float(input("Digite a largura: "))
area(largura, comprimento)



