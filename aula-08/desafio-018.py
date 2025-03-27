import math
n1 = float(input('digite um número:'))
n2 = math.cos(math.radians(n1))
n3 = math.sin(math.radians(n1))
n4 = math.tan(math.radians(n1))

print('o cosseno de {} é : {:.2f}'.format(n2))
print('o seno de {} é; {:.2f}'.format(n3))
print('o tangente de {} é: {:.2f}'.format(n4))