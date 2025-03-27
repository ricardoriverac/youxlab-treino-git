import math
n1 = float( input('Comprimento do cateto oposto: '))
n2 = float( input('Comprimento do cateto adjacente: '))

h = math.hypot(n1, n2)

print('A hipotenusa é {:.2f}'.format(h))