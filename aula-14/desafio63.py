num = int(input('Digite um número: '))
cont = fib = 0
fib1 = 1
while cont < num:
    print('{} {} '.format(fib,fib1),end='')
    fib += fib1
    fib1 += fib
    cont += 1