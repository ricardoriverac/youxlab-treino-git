from time import sleep
from random import randint 
print ('\033[1;35mVAMOS JOGAR PAR OU ÍMPAR!!!\033[0;0m')
jogador = 0
computador = 0
escolhaComputador = randint(1, 10)
vezes = 0
while True:
    print('Escolhe se vai querer \033[1;31mPAR\033[0;0m ou \033[1;33mÍMPAR\033[0;0m: ')
    print ('[1] Par')
    print('[2] Impar')
    jogador = int(input('Agora digite o número correspondido a sua escolha: '))
    print('ANALISANDO...')
    sleep(2 )
    numero = int(input('Escolha o número que quer jogar: '))
    print('-' * 40)
    soma = numero + escolhaComputador
    parOuNao = soma%2
    print(f'Vocẽ escolheu {numero} e o computador escolheu {escolhaComputador}.')
    print ('VERIFICANDO...')
    sleep (2)
    print (f'A soma {jogador} + {escolhaComputador} = {soma}.')

    if jogador == 1 and parOuNao==0:
        print ('\033[1;33mO JOGO VAI CONTINUAR\033[0;0m')
        vezes +=1

    elif jogador == 2 and parOuNao!=0:
        print('Você venceu.')
        print ('\033[1;33mO JOGO VAI CONTINUAR\033[0;0m')
        vezes +=1
    else:
        print('Você perdeu.')
        print ('\033[1;33mO JOGO ACABOU\033[0;0m')
        break
print (f'A quantidade de vezes que você venceu é {vezes}')
print ('hehehehehehehehehe')