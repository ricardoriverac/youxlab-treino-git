km=float(input('qual a distância em km? '))
if km>200:
    custo=km*0.45
    print('Sua passagem será {}'.format(custo))
else:
    custo=km*0.50
    print('Sua passagem será {}'.format(custo))