def fatorial(num=1):
    f=1
    for c in range( num, 0 , -1):
        f*= c
    return f

n=int(input('Digite um valor: '))
n1=int(input('Digite outro valor: '))
print(f'O valor {n} tem seu fatorial como {fatorial(n)}')
print(f'O valor {n1} tem seu fatorial como {fatorial(n1)}')


print('=' * 30)
def show():
    resp=str(input('Você quer que mostre o calculo ? [S/N]'))
    while resp  == 'Nn':
        break
    for c in range (n, 0 , -1 ):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ' , end=' ')
            else:
                print(f' = {fatorial(n)}' , end=' ')
    for c in range (n1, 0 , -1 ):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ' , end=' ')
            else:
                print(f' = {fatorial(n1)}' , end=' ')    

show()
