somadosProdutos = maisde1800 = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1 
    if cont == 1 :
        menor = preco
        barato = nome
    else:
        if preco < menor :
            menor = preco
            barato = nome
    if preco < preco :
        barato += nome
    if preco >= 1800:
        maisde1800 += 1
    somadosProdutos += preco
    opcoes = str(input('Quer continuar [S/N] ')).strip().upper()
    if opcoes != 'S' and opcoes != 'N':
        while True:
            opcoes = str(input('Quer continuar [S/N] ')).strip().upper()
            if opcoes == 'S' or opcoes == 'N':
                break
    if opcoes == 'N': 
        break
print(f'O total da compra foi {somadosProdutos}')
print(f'Temos {maisde1800} produtos custando mais de 1800.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
