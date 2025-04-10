valores = []

for indice in range(5):
    numero = int(input(f'Digite um número: '))
    valores.append(numero)

    if indice == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice} ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice} ', end='')