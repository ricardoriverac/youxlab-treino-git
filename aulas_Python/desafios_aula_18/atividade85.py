print('\033[1;34m-=-=-=-=-= Lista com pares e ímpares =-=-=-=-=-\033[m')
ListadeNúmeros = []
for c in range(1, 8):
    ListadeNúmeros.append(int(input(f'Digite o {c}°. número: ')))

print('=-'*20,'\nOs valores pares digitados foram:', sorted([n for n in ListadeNúmeros if n % 2 == 0]), end=' ')
print('\nOs valores ímpares digitados foram:', sorted([n for n in ListadeNúmeros if n % 2 == 1]), end=' ')
print()