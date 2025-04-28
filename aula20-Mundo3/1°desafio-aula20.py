#CALCULANDO ÁREA COM FUNÇÃO
print('    CONTROLE DE TERRENOS    ')
def valores(largura, comprimento):
    area=largura*comprimento
    print(f'A área do terreno {largura}x{comprimento} é de {area}m²')

largura=float(input('Largura (m): '))
comprimento=float(input('Comprimento (m): '))

valores(largura, comprimento)