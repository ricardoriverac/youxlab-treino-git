from math import sin,cos,tan,radians
a=float(input('Digite o ângulo que você deseja:'))
seno=sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a,seno))
cos=cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a,cos))
tan=tan(radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a,tan))