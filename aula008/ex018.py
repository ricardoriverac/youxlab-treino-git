from math import radians,sin,cos,tan
angulo =float(input('Digite o angulo que deseja: '))
seno =sin(radians(angulo))
print('O angulo de {} tem seno de {:.2f} '.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f} '.format(angulo,cosseno))
tangente =tan(radians(angulo))
print('O angulo de {} tem tangente de {:.2f} '.format(angulo,tangente))