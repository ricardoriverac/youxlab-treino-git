from random import randint 
import time
jogadas = ["PEDRA" ,"PAPEL" ,"TESOURA"]
computador = randint(0,2)
print("""'ESCOLHA SUA JOGADA'
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input('Digite a opção: '))
time.sleep(1)
print('\033[1;36mJO\033[m')
time.sleep(1)
print('\033[1;36mKEN\033[m')
time.sleep(1)
print('\033[1;36mPOOO!!!\033[m')
print(f'Computador jogou {jogadas[computador]}')
print(f'Jogador jogou {jogadas[jogador]}')
if computador == 0:
    if jogador == 0:
        print('\033[7;30;47mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mVITÓRIA')   
    elif jogador == 2:
        print('\033[1;31mDERROTA\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[1;31mDERROTA\033[m')
    elif jogador == 1:
        print('\033[7;30;47mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mVITÓRIA\033[m')   
elif computador == 2:
    if jogador == 0:
        print('\033[1;32mVITÓRIA\033[m')
    elif jogador == 1:
        print('\033[1;31mDERROTA\033[m')
    elif jogador == 2:
        print('\033[7;30;47mEMPATE\033[m')   
#{jogadas[computador]}
#lista a jogada que o computador pode jogar 