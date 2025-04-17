num =  [[], []]
valor = 0 
for c in range ( 1 , 8):
    valor=int(input(f'Digite o valor {c} '))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Pares {num[0]}')
print(f'Impares {num [1]}')