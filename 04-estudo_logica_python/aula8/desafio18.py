import math
angulo=float(input(' digite um angulo:'))
seno= math.sin(math.radians(angulo))
print(' o agulo de {},tem o seno de {:.2f}'.format(angulo, seno))
cosseno= math.cos(math.radians(angulo))
print(' o angulo de {},tem cosseno de {:.2f}'.format(angulo, cosseno))
tangente= math.tan(math.radians(angulo))
print ('angulo de {}, tem a tangente de {:.2f}'.format(angulo, tangente))