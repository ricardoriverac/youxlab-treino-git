from math import factorial
numero= int(input('Digite um número para calcular seu fatorial: '))
c= numero
fatorial= 1
print('Calculando {}! '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}')