nome = (input('Qual seu nome?'))
print('Prazer te conhecer {:+^30}!'.format(nome))

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {}, \n o produto é {}, e a divisão é {:.3f}'. format (s,m,d), end=' ')
print('Divisão inteira é {}, e a pôtencia é {}'. format (di,e))