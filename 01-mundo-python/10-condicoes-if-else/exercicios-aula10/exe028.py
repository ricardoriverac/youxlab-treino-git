from random import randint
import time
computador = randint(0,5)
print('\033[0;34;46m... Estou pensando em um número entre 0 e 5. Tente adivinhar...\033[m')
jogador = int(input('Em que número pensei: '))
print('\033[0;34mPROCESSANDO........\033[m')
time.sleep(1)
if jogador == computador :
    print('\033[32mVITÓRIA\033[m')
    print('PERDI, ops... parabéns')
else:
    print('\033[31mDERROTA\033[m')
    print(f'GANHEI, pensei no {computador} e não no {jogador}') 