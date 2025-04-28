valores = [[], []]

for c in range(0, 7):
    numero = int(input('Digite um valor: '))

    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

print(f'Os valores pares são {sorted(valores[0])} e os ímpares são {sorted(valores[1])}')