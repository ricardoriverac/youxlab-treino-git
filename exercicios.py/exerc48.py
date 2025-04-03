print('Entre 1 e 500 existem números ímpares mútiplos de 3.')
print('Vamos ver a soma entre eles? ')
soma = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
     soma = soma + m
print('A soma de todos os valores solicitado é {}.'. format(soma))
