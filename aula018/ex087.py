matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares =maior = somaColunas =0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor: {linha},{coluna}: '))

for linha in range(0,3):
    for coluna in range(0,3):

        print(f'[{matriz[linha][coluna]:^5}] ', end='')
        if matriz [linha] [coluna] % 2 == 0:
            somaPares += matriz [linha] [coluna]


print(f'A soma dos pares é {somaPares}')
for linha in range(0,3):
    somaColunas += matriz [linha] [2]

print(f'A somadas dos valores da terceira coluna é: {somaColunas}')




