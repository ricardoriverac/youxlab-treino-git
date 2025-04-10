matriz = [[], [], []]
par = col3 = 0  # números pares & coluna 3
for x in range(3):
    for y in range(3):
        matriz[x].append(int(input(f'Digite um valor para posição [{x},{y}]: ')))
        par += matriz[x][y] if matriz[x][y] % 2 == 0 else 0
        col3 += matriz[x][y] if y == 2 else 0
print('-' * 35, *matriz, sep='\n')  # Mostra a matriz
print('-' * 35, f'\nA soma dos números pares é {par}')
print(f'A soma dos números da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')