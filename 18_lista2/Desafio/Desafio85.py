valores = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digiddtados foram: {sorted(valores[1])}')