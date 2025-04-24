def fatorial(num=1):
    f=1
    for c in range(num , 0 , -1):
        f*= c
    return f

n=int(input('Digite um valor: '))
print(f'O valor {n} tem seu fatorial como {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False



num=int(input('Digite um valor: '))
if par(num):
    print('é par')
else:
    print('Não é par')