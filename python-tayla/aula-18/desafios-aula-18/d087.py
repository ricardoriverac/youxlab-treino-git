matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = []
numeroTerceiraColuna = maior = 0

for l in range(3):
    for c in range(3):
        numero = int(input('Digite um valor: '))
        matriz[l][c] = numero

        if numero % 2 == 0:
            par.append(numero)

        if c == 2:
            numeroTerceiraColuna += matriz[l][c]
maior = max(matriz[1])

print('-=' * 20)
for o in range(3):
    print(matriz[o])
print('-=' * 20)

print(f'A soma dos números pares é {sum(par)}')
print(f'A soma dos valores da terceira coluna é {numeroTerceiraColuna}')
print(f'O maior valor da segunda linha é {maior}')