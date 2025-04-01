from math import hypot
catetoO= float(input('Comprimento do cateto oposto: '))
catetoA= float(input('Comprimento do vateto adjacente: '))
hipotenusa= hypot(catetoO, catetoA)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))