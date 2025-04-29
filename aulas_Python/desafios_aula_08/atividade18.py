import math
an = float(input('Digite o ângulo que deseja aqui: '))

se = math.sin(math.radians(an))
print('O ângulo do seno é: {:.2f}'.format(se))

cos = math.cos(math.radians(an))
print('O ângulo do cosseno é: {:.2f}'.format(cos))

tan = math.tan(math.radians(an))
print('O ângulo da tangente é: {:.2f}'.format(tan))
