def fatorial(a, b=True):
    c = 1
    for i in range(a, 0, -1):
        c *=i 
        if b == True:
            print(i, end=' ')
            if i != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return c

a = int(input(('Digite um número para o calculo da fatorial: ')))
print(fatorial(a))