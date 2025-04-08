numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

print(f'\nCalculando {numero}! = ', end='')

for c in range(numero, 0, -1):
    print(f'{c}', end=' x ' if c > 1 else ' = ')
    fatorial *= c

print(f'{fatorial}')
