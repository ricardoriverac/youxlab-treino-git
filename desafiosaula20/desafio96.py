def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno \033[35m{largura} x {comprimento}\033[m é igual a \033[32m{a}m²\033[m ')


print('-='*20)
print('\033[35mCONTROLE DE TERRENOS\033[m')
print('-='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
