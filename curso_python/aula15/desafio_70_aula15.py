totalGasto = 0
maisDeMil = 0
maisBarato = 0
contador = 0
nomeBarato = ''

while True:
    print ('><' * 9)
    print ('LOJA SUPER BARATÃO')
    print ('><' * 9)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1
    totalGasto += preco

    if contador == 1 or preco < maisBarato:
        maisBarato = preco
        nomeBarato = produto

    if preco > 1000:
        maisDeMil += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? ')).strip().upper()
    if resposta == 'N':
        break

print (f'O total da compra é de R$ {totalGasto:.2f}')
print (f'Temos {maisDeMil} produto(s) acima de R$ 1000 ')
print (f'O produto mais barato é {nomeBarato} que custa R$ {maisBarato:.2f} ')