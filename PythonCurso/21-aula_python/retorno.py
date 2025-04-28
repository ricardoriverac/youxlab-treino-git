def contador2(a=0, b=0, c=0):
    s = a + b + c
    return s



r1 = (contador2(2, 1))
r2 = ( contador2(3,5))

print(f'OS resultados foram {r1} e {r2}')



def fatorial(num =1):
    f = 1
    for c in range(num, 0, -1):
        f *=c
    return f

f1 = fatorial(5)
f2 = fatorial(7)
f3 = fatorial()

print(f'OS resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número '))
if par(num):
    print('É par!!')
else:
    print('Não é par!! ')