lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input("\033[38;5;213mNome:\033[0m ")).title().strip())
    dados.append(float(input("\033[35;5;213mPeso:\033[0m ")))

    if len(lista) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    r = input('Deseja continuar? [S/N] ').strip().upper()
    if r == 'N':
        break
print(f'\nAo todo foram cadastradas {len(lista)} pessoas.')

print(f'\033[32mMaior peso foi {maior} Kg. Peso de\033[0m ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'\033[34mMenor peso foi {menor} Kg. Peso de\033[0m ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
ordenada = sorted(lista, key=lambda x: x[1])
print('\n\033[36mPessoas da mais leve para a mais pesada:\033[0m')
for pessoa in ordenada:
    print(f'{pessoa[0]} - {pessoa[1]} Kg')
