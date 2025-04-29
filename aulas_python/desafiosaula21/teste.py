def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3} ')

def ParImpar (n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Digite um número: '))
if ParImpar(numero):
    print('É par ')
else:
    print('É ímpar ')
    