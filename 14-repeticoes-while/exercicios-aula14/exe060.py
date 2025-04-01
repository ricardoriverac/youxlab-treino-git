#RESOLUÇÃO GUANABARA

#num = int(input('Digite um  número qualquer: '))
#c = num
#fa = 1
#print(f'Calculando o fatorial do {num}! ', end='')
#while c > 0:
#    print(f'{c}', end='')
#    print(f'x' if c > 1 else '=' , end='')
#    fa *= c
#    c -= 1
#print(fa)

#Minha resolução com for
from math import factorial
num = int(input('Digite um número qualquer: '))
fa = factorial(num)
print(f'{num}x', end='')
for c in range(num -1,-1,-1):
    print(f'{c}', end='')
    print(f'x' if c > 0 else '=', end='')
print(f' O fatorial desse número será de {fa}')


