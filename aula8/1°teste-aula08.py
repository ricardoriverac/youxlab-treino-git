#Calculando raiz quadrada 
import math
n=int(input('Digite um número:'))
raiz=math.sqrt(n)
print(f'a raiz quadrada de {n} é {raiz}!')


#Pode ser feito assim também se quiser apenas uma função da biblioteca
from math import sqrt
n=int(input('Digite um número:'))
raiz= sqrt(n)   # não precisa do comando math. pois a função já tinha sido selecionada a cima 
print(f'a raiz quadrada de {n} é {raiz}!')