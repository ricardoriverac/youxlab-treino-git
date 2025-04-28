from math import hypot

co = float(input('Digite o compriemnto do cateto oposto'))
ca =  float(input('Digite o comprimento do cateto adjacente'))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'. format(h1)) 