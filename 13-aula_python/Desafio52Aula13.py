num=int(input('Digite num :'))
tot= 0
for c in range(1 , num + 1):
    if num% c ==0:
        print('\033[33m', end =' ')
        tot+= 1
    else:
        print('\033[33m', end =' ')
    print('{}'.format(c),end ='')
print('\n\033[O número {}  foi divisivel  {}  vezes'.format(num, tot))
if tot ==2:
    print('Por isso é um primo')
else:
    print('Não é primo')