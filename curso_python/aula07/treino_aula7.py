# a=5+3*2
# print(a)

# a=18%2
# print(a)

# a=122%3
# print(a)

# a=4**3
# print(a)

# a=pow(4,3)
# print(a)

# a = 81**(1/2)
# print (a)

# a = 25**(1/2)
# print (a)

# a = 127**(1/3)
# print (a)

# a = 'Oi' *5
# print (a)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print ('Divisão inteira {} e potência {}'.format(di, e))