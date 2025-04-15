def area (largura, comprimento):
        total = largura * comprimento
        print(f'A área de um terreno {largura} x {comprimento} é de {total}m²'.center(45))
def titulo(txt):
    print('-'*45)
    print(txt)
    print('-'*45)

titulo('Controle de Terrenos')
area(float(input('LARGURA (m): ')),
     float(input('COMPRIMENTO (m): ')))