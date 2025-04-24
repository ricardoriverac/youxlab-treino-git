matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
for linha in range(3):
    soma_terceira_coluna += matriz[linha][2] 

maior_segunda_linha = max(matriz[1])  


print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^3} ]", end=' ')
    print()
print(f"\nA) A soma de todos os valores pares é: {soma_pares}")
print(f"B) A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"C) O maior valor da segunda linha é: {maior_segunda_linha}")