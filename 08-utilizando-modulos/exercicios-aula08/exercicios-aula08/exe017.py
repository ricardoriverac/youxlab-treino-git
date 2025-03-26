from math import hypot
ca = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(ca,ad):.2f}')
