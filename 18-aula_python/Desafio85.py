numero = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-='*35)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares  digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')