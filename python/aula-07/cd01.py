n1 = int (input ('Digite um valor:'))
n2 = int (input('Outro valor:'))
s = n1 + n2
m = n1 - n2 
d = n1 / n2 
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, o produto é {}, e a divisão é {}'.format(s, m, d), end='>>>')
print ('Divisão inteira {} e potencia {}'.format (di,e))