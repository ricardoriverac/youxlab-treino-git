# numero = int(input('Digite um número inteiro: '))
# fatorial = numero
# resultado = numero
# while fatorial != 1:
#     fatorial = fatorial - 1
#     resultado = fatorial * resultado
# print(f'O fatorial do número {numero} é {resultado}')

from math import factorial
n = int((input('Digite um número inteiro: ')))
fatorial = factorial(n)
print(f'O fatorial do número {n} é {fatorial}')