num =int(input('Me diga um valor para saber se e primo: '))
primos = 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m ',end= ' ') 
        primos += 1
    else: 
        print('\033[31m',end =' ')
    print(f'{c}', end= ' ')
if primos ==2:
    print('Ele e um número primo ')
else:
    print('Não e um numero primo,pois possui {} divisores '.format(primos))