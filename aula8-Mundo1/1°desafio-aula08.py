#porção inteira de um n° decimal
from math import trunc
num =float(input('Digite um número decimal:'))
resultado=trunc(num)
print(f'A porção inteira de {num} é {resultado}')