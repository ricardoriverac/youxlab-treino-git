matriz = []
somanumPar, somaTercCol = 0, 0 
for linha in range(3):
    valor = []
    for coluna in range(3):
        valor.append(int(input(f'Informe um valor para [{linha}, {coluna}]: ')))
    matriz.append(valor)
print(f'\n{"MATRIZ":^32}\n')
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somanumPar += matriz[linha][coluna]
    print()
for linha in range(3):
    somaTercCol += matriz[linha][2]
print('-' * 32)
print(f'\033[38;5;196mSoma dos valores pares: {somanumPar}')
print(f'\033[38;5;208mSoma dos valores da 3º coluna: {somaTercCol}')
print(f'\033[38;5;226mMaior valor da segunda linha: {max(matriz[1])}')