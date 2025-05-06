#fazer em casa: 
maior= 0
menor= 0
for a in range(1, 6): 
    peso= float(input('Informe seu peso em kg: '))
    if a == 1:
        maior= peso
    else:
        if peso > maior:
            maior= peso
    if a == 1:
        menor= peso
    else:
        if peso < menor:
            menor= peso
                
print(f'O maior peso lido foi {maior}')
print(f'O menor peso foi {menor}')