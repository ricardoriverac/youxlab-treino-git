total = maisdemil = produtos =  0
precobarato = float('inf')
nomebarato = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço deste produto? R$'))
    continuar = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    total += preco
    produtos += 1

    if preco > 1000:
        maisdemil += 1
    if preco < precobarato:
        precobarato = preco
        nomebarato = nome

    if continuar == 'N':
        break
print(f'O total de compras foi R${total:.2f}')
print(f'Tem {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato}, custando R${precobarato:.2f}.')