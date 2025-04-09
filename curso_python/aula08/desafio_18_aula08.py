import math
angulo = int(input('Qual é o valor do ângulo em graus? '))
rad = math.radians(angulo)
print (f'O seno de {angulo}° é {math.sin(rad):.2f}')
print (f'O cosseno de {angulo}° é {math.cos(rad):.2f}')
print (f'O tangente de {angulo}° é {math.tan(rad):.2f}')