from math import sin, cos, tan, radians, sqrt
n1 = int(input("insira um número: "))
n2 = int(input('insira outro número: '))
h2 = sqrt(n1**2 + n2**2)

ang = radians(h2)
s = sin(ang)
c = cos(ang)
t = tan(ang)
print(f'Com o angulo de {h2}º, o seno é {s}, o cosseno é {c} e a tangente é {t}')