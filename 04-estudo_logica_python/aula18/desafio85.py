lista = [[], []]
for c in range(7):
    numero= int(input(f'Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('--'* 40 )
print(f'Todos os valores são {lista}.')
print(f'Valores pares digitados foram: {sorted(lista[0])}')
print(f'Valores ímpares digitados foram: {sorted(lista[1])}')