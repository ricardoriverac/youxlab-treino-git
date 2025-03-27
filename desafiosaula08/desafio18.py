from math import radians, sin, cos, tan
n = float(input('Qual é o ângulo que você deseja?: '))
seno = sin(radians(n))
print ('O ângulo {} tem o SENO de {:.2f}'.format(n,seno))
cos = cos(radians(n))
print ('O ângulo {} tem o CASSENO de {:.2f}'.format(n,cos))
tan = tan(radians(n))
print ('O ângulo {} tem o TANGENTE de {:.2f}'.format(n,tan))
