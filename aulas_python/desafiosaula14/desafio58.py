from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador "PENSAR" 
numero = 0
palpites = 0

while numero != computador:
    numeroAposta = int(input('Tente descobrir qual número escolhi, digite um número de a 0 a 10: '))
    palpites+=1
    numero=numeroAposta
print('{}PARABÉNS!{} Você acertou depois de {} tentativas!!! '.format('\033[35m', '\033[m', palpites))
