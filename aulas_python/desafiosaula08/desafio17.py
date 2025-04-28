from math import hypot
n = float(input('Comprimento do cateto oposto: '))
nn = float(input('Comprimento do cateto adjacente: '))
hi= (n ** 2 + nn ** 2)** (1/2)
print ('A hipotenusa é {:.2f}'.format(hi))

n = float(input('Comprimento do cateto oposto: '))
nn = float(input('Comprimento do cateto adjacente: '))
hi = hypot (n,nn)
print ('A hipotenusa vai medir {:.2f}'.format(hi))
