text = int(input('Distância da viagem: '))
preco1 = text * 0.50
preco2 = text * 0.45
if text <= 200:
    print(f'o preço da sua passagem será de R${preco1}')
else:
    print(f'o preço da sua passagem será de R&{preco2}')