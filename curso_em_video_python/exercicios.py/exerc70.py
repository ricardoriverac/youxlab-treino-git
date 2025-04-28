from time import sleep
nome = ' '
preco = 0
produtos = ' '
lista = [ ]
maisde = 0
maisBarato = ' '
menorPreco = 0
contador = 0
continuar = ''
print('\033[1mVOCÊ ESTÁ FAZENDO COMPRAS!!\033[0;0m')
sleep(0.5)
print('\033[1;35m--LOJA DA ANINHA--!!\033[0;0m')
sleep (0.5)
print('-' * 40)
sleep(0.5)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Digite o preco: R$'))
    lista.append(preco)
    soma = sum(lista)
    menor = min(lista)
    if contador == 0:
            menorPreco = preco
    if menorPreco >= preco:
            menorPreco = preco
            maisBarato = produto
    continuar = str(input('Quer continuar [S/N]')).upper()
    print('-' *20)

    while 'Ss' in continuar:
        if continuar not in "Ss" and 'Nn':
         continuar = int(input("Tente de novo: "))
        if continuar in 'Ss':
         print('Olha só, ta rico! Compre mais então MUHAHAHAHAHA')
        if preco > 1000:
            maisde+=1
        if continuar in 'Nn':
            print('POBREEEEEEEEE')
    break
    contador +=1
print(f'O total que você gastou foi R${soma}')
print(f'A quantidade de produtos que custam mais de R$1000 é {maisde}')
print(f'O produto mais barato custou R${menor}, é o {maisBarato}')