lista = [[], []]
numero = 0
for c in range (1, 7+1):
    numero = int(input(f'Digite o {c}o número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    elif numero % 2 == 1:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Os números pares foram {lista[0]}')
print(f'Os números impares foram {lista[1]}')
    