import math
oposto = int(input('Qual o valor do cateto oposto? '))
adjacente = int(input('Qual o valor do cateto adjacente? '))
hipotenusa = adjacente**2 + oposto**2
comprimento = hipotenusa**(1/2)
print (comprimento)