listval = []
maior = 0
menor = 0
for c in range(0,5):
    listval.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listval[c]
    else:
        if listval[c] > maior:
            maior = listval[c]
        if listval[c] < menor:
            menor = listval[c]
print('=='*30)
print(f'Você digitou os valores {listval}')
print(f'O maior valor digitado foi {max(listval)} nas posições ')
for i, v in enumerate(listval):
    if v == maior:
        print(f'{i}... ', end = '')
print()
print(f'O menor valor digitado foi {min(listval)} nas posições')
for i, v in enumerate(listval):
    if v == menor:
        print(f'{i}... ', end = '')
print()