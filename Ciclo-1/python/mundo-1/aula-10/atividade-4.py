km = int(input('Distância da viagem: '))
preco1 = km * 0.50
preco2 = km * 0.45
if km <= 200:
    print(f'o preço da passagem erá R${preco1}')
else:
    print(f'o preço da passagem será R&{preco2}')