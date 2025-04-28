''' from math import trunc
num = float(input('Digite seu valor'))
print('O valor que você digitou foi {} e a sua porção inteira é {}'. format (num, trunc(num))) '''

num = float(input('Digite um valor'))
print('O valor que você digitou foi {} e a sua porção inteira é {}'. format (num, int(num)))