#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#Calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
cal = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(cal))