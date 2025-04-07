import math
num = int(input('Digite um número:'))
fa = math.factorial(num)
fatorial = 1
for i in range (1, num +1):
    fatorial *= i
for c in range(num, 0, -1):
    print(f'{c}x', end= '')
    print(f'{fatorial}')
#print(f'O fatorial de {num}! é {c} {fatorial}')
