lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior =linha = 0

for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'\033[36mDigite um numero para [{l},{c}\]\033[0m: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]

for l in range(3):
    maior += lista[l][2]

for col in range(3):
    if linha == 0:
        linha = lista[1][col]
    elif linha < lista[1][col]:
        linha = lista[1][col]
print(lista)


for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]', end='  ')
    print()
print('---' * 40)
print(f'A soma de todos os numeros pares é {par}')
print(f'A soma dos numero da terceira coluna totaliza {maior}')
print(f'O maior numero da segunda linha é {linha}')