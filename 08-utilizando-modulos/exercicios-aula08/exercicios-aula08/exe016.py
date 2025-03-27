#floor significa arredondar um número para baixo , ceil para cima 
from math import floor
n = float(input('Digite um número real:'))
print(f'O valor digitado é {n} e a sua porção inteira é {n.__floor__()}')