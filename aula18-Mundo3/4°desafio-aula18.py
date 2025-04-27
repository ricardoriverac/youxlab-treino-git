#MAIS UM POUCO DE MATRIZ
matriz=[[0,0,0],[0,0,0],[0,0,0]]
somaPar=somaColuna=maior=0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para {[linha]}, {[coluna]}: '))
print('Sua matriz:')
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
        if matriz[linha][coluna]%2==0:
            somaPar+=matriz[linha][coluna]
    print()
print(f'A soma dos números pares é {somaPar}')
for linha in range (0,3):
    somaColuna+=matriz[linha][2]
print(f'A soma dos valores da 3° coluna é {somaColuna}')
for coluna in range (0,3):
    if coluna==0 or maior<matriz[1][coluna]:
        maior=matriz[1][coluna]
print(f'O maior valor da 2° linha é o {maior}')

