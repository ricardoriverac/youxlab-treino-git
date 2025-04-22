def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do seu terreno {largura}x{comprimento} é de {a}m²')

def linha():
    print('\033[1m—\033[m' * 35)

linha()
print('\033[1;33mControle de Terrenos\033[m')
linha()
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))