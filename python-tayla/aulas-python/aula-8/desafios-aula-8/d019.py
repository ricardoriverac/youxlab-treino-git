from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo qualquer em graus: '))
graus = radians(angulo)
seno = sin(graus)
cosseno = cos(graus)
tangente = tan(graus)
print(f'O valor do seno é {seno:.2f}, do cosseno é {cosseno:.2f} e o tangente é {tangente:.2f}')