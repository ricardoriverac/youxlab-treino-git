import math
c1 = float(input('Digite o comprimento de um cateto op:'))
c2 = float(input('Digite outro comprimento de um cateto adj:'))
hip = c1**2 
hip1 = c2**2
hipo = hip+hip1
hipo1 = math.sqrt(hipo)
print('A hipotenusa do triângulo retângulo é: {:.2f}'.format(hipo1))
