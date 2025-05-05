total=totalMil=menorPreco=contador= 0
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço: R$'))
    contador += 1
    total += preco
    if preco > 1000:
        totalMil += 1
    if contador == 1:
            menorPreco = preco
    else:
        if preco < menorPreco:
            menorPreco = preco
    resposta= ' '
    while resposta not in 'SN':
        resposta= str(input('Quer continuar? [S/N] ')).upper() .capitalize()
    if resposta == 'N':
        break
print('{:_^40}'.format('VOLTE SEMPRE!'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menorPreco:.2f}')