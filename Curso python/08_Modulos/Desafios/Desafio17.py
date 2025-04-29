'''co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente "))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print("Hipotenusa e {}, ".format(hi))'''
import math 
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co,ca)
print("A hipotenusa e {:.2f},".format(hi))