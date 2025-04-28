n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele \033[1;34mÉ PRIMO!\033[m')
else:
    print('E por isso ele \033[1;31mNÃO É PRIMO!\033[m')