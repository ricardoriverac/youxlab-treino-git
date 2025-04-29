numero = int(input('Digite um número: '))
total = 0
for p in range(1, numero + 1):
    if numero % p == 0:
        print ('\033[1;33m', end=' ')
        total += 1
    else:
        print ('\033[m', end=' ')
    print (f'{p}', end=' ')
print (f'\n\033[mO número {numero} foi dividido {total} vezes ')
if total == 2:
    print (f'O número {numero} é primo! ')
else:
    print (f'O número {numero} não é primo! ')