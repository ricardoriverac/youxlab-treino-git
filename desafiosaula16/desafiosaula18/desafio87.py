matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaTerceira = maior = somaSegunda = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor
print('-='*30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ', end='')
        if matriz[linha] [coluna] % 2 == 0:
            soma+=matriz[linha] [coluna]
        if coluna == 2:
            somaTerceira += matriz[linha][coluna]
        if coluna == 1:
            somaSegunda += matriz[linha][coluna]
        if coluna == 0:
            maior = matriz[1][coluna]
        elif matriz[1][coluna]>maior:
                maior = matriz[1][coluna]
    print()
numeroDoMeio = matriz[1][1]
print()
print('-='*30)
print(f'A \033[36msoma dos números pares\033[m é {soma}')
print(f'A \033[35msoma da terceira coluna\033[m é {somaTerceira}')
print(f'A \033[34msoma da segunda coluna\033[m é {somaSegunda}')
print(f'O \033[33mmaior número da segunda linha\033[m é {maior}')
print(f'O \033[32mnúmero do meio\033[m é {numeroDoMeio} ')


