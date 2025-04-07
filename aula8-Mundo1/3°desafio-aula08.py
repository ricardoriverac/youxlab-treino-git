from math import radians, sin, cos, tan
angulo=float(input('Digite o ângulo:'))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print('Seno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(seno,cosseno,tangente))