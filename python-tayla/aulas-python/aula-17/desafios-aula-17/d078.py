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
print(f'Você digitou os valores \033[1;35m{valores}\033[m')
print(f'O maior valor digitado foi \033[1;36m{maior}\033[m nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'\033[1;31m{indice}\033[m ', end='')

print(f'\nO menor valor digitado foi \033[1;33m{menor}\033[m nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'\033[1;31m{indice}\033[m ' '... ' , end='')