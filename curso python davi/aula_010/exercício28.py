from random import randint
import time
number00 = randint(0,5)
print('diga um número de 0 a 5 ')
jogador = int(input('qual o número?: '))
print('...')
time.sleep(1)
if jogador == number00 :
    print('...')
    print('acertou!')
else:
    print('foi por pouco')
    print(f'perdeu, era o {number00} e não o {jogador}') 