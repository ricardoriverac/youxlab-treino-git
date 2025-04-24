num = int(input('Digite o número: '))
tot = 0 
for c in range(1 , num +1):
    if num  % c == 0:
        tot += 1
        print('\033[32m', end=" ")
    else:
        print('\033[31m', end=" ")
    print(f'{c}', end=' ')
print(f'\n\033[30mO número {num} foi divisivél {tot} vezes')
if tot == 2 :
    print('É por isso ele é número primo')
else:
    print('É por isso ele não é número primo')