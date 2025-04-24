total = produtos_mais_1000 = produtos_comprados = preço_produto_mais_barato = 0
from time import sleep
print('-'*50)
print('        LOJA')
print('-'*50)
while True:
    nome_produto = str(input('Nome do produto: ')).strip().lower()
    preço_produto = float(input('Preço do produto: ').strip())
    produtos_comprados += 1
    total += preço_produto
    if preço_produto > 1000:
        produtos_mais_1000 += 1
    if produtos_comprados == 1:
        nome_produto_mais_barato = nome_produto
        preço_produto_mais_barato = preço_produto
    else:
        if preço_produto_mais_barato > preço_produto:
            preço_produto_mais_barato = preço_produto
            nome_produto_mais_barato = nome_produto

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('\033[;31mOpção Inválida! Tente de novo.\033[m')
        else:
            break
    if continuar == 'N':
        print(f'\033[;33mFinalizando as compras...\033[m')
        break
print('-'*50)
print(f'Total: {total}')
print(f'Produtos mais de R$1000: {produtos_mais_1000}')
print(f'Produto mais barato: {nome_produto_mais_barato} custando {preço_produto_mais_barato}')
print('-'*50)