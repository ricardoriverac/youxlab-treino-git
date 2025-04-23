valores = [[], []]
for cont in range(7):
    numero = int(input(f'Informe o {cont + 1}º número: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
valores[0].sort() 
valores[1].sort()
print('-' * 40)
print(f'\n\033[\033[38;5;178mTODOS VALORES: {valores}\033[0m')
print(f'\n\033[38;5;218mVALORES PARES DIGITADOS: {valores[0]}\033[0m')
print(f'\033[38;5;198mVALORES ÍMPARES DIGITADOS: {valores[1]}\033[0m')