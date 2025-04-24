print('Calculadora de fatorial!')

n = int(input('Digite um número para saber o seu fatorial: '))
c = 1
fatorial = n

while c < n:
    fatorial *= (n - c)
    c += 1
print('O fatorial de {} é {}.'.format(n, fatorial))