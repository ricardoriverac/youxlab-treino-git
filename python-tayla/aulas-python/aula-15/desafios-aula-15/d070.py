totalGasto = 0
milMais = 0
nomeMaisBarato = ''
precoMaisBarato = 0
primeiroPreco = True

print('=' * 20)
print('\033[1;33mLOJA SUPER BARATÃO\033[m')
print('=' * 20)

while True:
    produto = input('Qual o nome do produto? ')
    preco = float(input('Qual seu valor? R$'))
    
    totalGasto += preco

    if preco > 1000:
        milMais += 1

    if primeiroPreco:
        precoMaisBarato = preco
        nomeMaisBarato = produto
        primeiroPreco = False

    if preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBarato = produto

    pergunta = input('Quer continuar? [S/N] ').upper()
    print('\033[1m-=\033[m' * 10)

    if pergunta == 'N':
        break

print('\033[1m-\033[m' * 37)
print(f'O total gasto na compra foi R${totalGasto:.2f}')
print(f'{milMais} produtos custam mais de R$1000')
print(f'O produto mais barato foi {nomeMaisBarato}')
print('\033[1m-\033[m' * 37)