def arealec():
    arealec = area[0] * area[1]
    print(f'A area de {area[0]}x{area[1]} e {arealec}m²')



#programa principal
print('Controle de terrenos')
print('-='*30)
area = list()
area.append(float(input('Largura (m): ')))
area.append(float(input('Comprimento (m): ')))
arealec()