import math
a1 = int(input('Digite um valor de ângulo:'))
se = math.sin(math.radians(a1))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a1, se))
co = math.cos(math.radians(a1))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a1, co))
tan = math.tan(math.radians(a1))
print('O ângulo {} tem o TANGENTE de {:.2f}'.format(a1,tan))