lista = [[], []]
pares = impares = 0
for c in range (1, 8):
    valor = (int(input(f'Digite o {c}ª valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)

print(f'Os \033[35mnúmeros pares\033[m são {sorted(lista[0])}')
print(f'Os \033[36mnúmeros ímpares\033[m são {sorted(lista[1])}')
