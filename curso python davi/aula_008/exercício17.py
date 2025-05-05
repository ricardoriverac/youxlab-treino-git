import math
ca = float(input('Comprimento do cateto adjacente:'))
co = float(input('Comprimento do cateto oposto:'))
cal = math.hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(cal))