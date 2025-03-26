from math import hypot
c1=float(input('Qual o comprimento do cateto oposto? '))
c2=float(input('Qual o comprimento do cateto adjascente? '))
hi=hypot(c1,c2)
print('De acordo com os cálculos, a hipotenusa mede {:.2f}'.format(hi))