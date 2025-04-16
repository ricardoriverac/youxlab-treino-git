def titulo(txt):
    print('-'*50)
    print(txt)
    print('-'*50)


titulo('Controle de Terrenos'.center(50))

# largura = int(input('LARGURA (m): '))
# comprimento = int(input('COMPRIMENTO (m): '))

# def area(largura, comprimento):
#     a = largura * comprimento
#     print(f'A área de um terreno de {largura}m e {comprimento}m é igual a {a}m²')
#area(largura, comprimento)

def area():
    largura = int(input('Largura (m):'))
    comprimento = int(input('Comprimento (m)'))
    a = largura * comprimento
    print(f'A área de um terreno com a largura de {largura}m e o comprimento de {comprimento}m é igual a {a}m²')

area()