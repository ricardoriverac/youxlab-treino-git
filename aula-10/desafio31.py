km = float(input('Qual a distância da sua viajem? '))
preço = km * 0.5
preço2 = km * 0.45

if km < 200:
    print(f'O custo da passagem é igual a R${preço:.2f} .')
else:
    print(f'O custo da passagem é igual a R${preço2:.2f} .')
