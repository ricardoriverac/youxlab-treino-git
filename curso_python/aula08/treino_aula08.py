import math
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print ('A raiz de {} é igual a {}'.format(numero, raiz))

# Arredondar o valor para cima
import math
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print ('A raiz de {} é igual a {}'.format(numero, math.ceil(raiz)))

# Arredondar o valor para baixo
import math
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print ('A raiz de {} é igual a {}'.format(numero, math.floor(raiz)))

# Mostrar a formatação com X casas decimais
import math
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print ('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

# Selecionar um tipo de módulo
from math import sqrt
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print ('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

# Selecionar dois ou mais tipos de módulos
from math import sqrt, floor
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print ('A raiz de {} é igual a {:.2f}'.format(numero, floor(raiz)))

# Fazer com que o computador me diga um número
import random
numero = random.random() 
# ou numero = random.randit(1, 10) para o computador escolher um número 
# inteiro de um até dez
print (numero)