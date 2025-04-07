addnumeros = list()
pares = list()
impares = list()
for c in range(1,8):
    numeros = int(input(f'Digite {c}° valor: '))
    addnumeros.append(numeros)
    if numeros % 2 == 0 :
        pares.append(numeros)
        
    if numeros % 2 == 1:
        impares.append(numeros)
print(f'Os números pares foram {sorted(pares)}')
print(f'Os números impares foram {sorted(impares)}')