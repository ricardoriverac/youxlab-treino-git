def area():
    comprimento = (float(input('Comprimento: ')))
    largura = (float(input('Largura: ')))
    a = comprimento * largura
    print(f'A área do terreno é de {a}m² quadrados')

def cabecalho():
    print()
    print('----- Controle de terreno -----')
    print()

cabecalho()
area()