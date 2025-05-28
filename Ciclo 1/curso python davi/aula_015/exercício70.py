listaprod = []
listapreco = []
while True:
    produto = str(input('nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    listaprod += [produto]
    listapreco += [preco]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${sum(listapreco):.2f}')
print(f'temos {len([i for i in listapreco if i > 1000])} produto(s) custando mais que R$1.000,00')
print(f'o produto mais barato foi {listaprod[listapreco.index(min(listapreco))]} e custou R${min(listapreco)}')