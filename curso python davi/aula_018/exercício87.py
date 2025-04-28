matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^3} ]", end=" ")
    print()
for linha in range(3):
    soma_terceira_coluna += matriz[linha][2]
maior_segunda_linha = max(matriz[1])
print(f"\nSoma de todos os valores pares: {soma_pares}")
print(f"Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"Maior valor da segunda linha: {maior_segunda_linha}")