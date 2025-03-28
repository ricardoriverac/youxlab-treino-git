import time
from random import randint
print('\033[35mTABUADA 2.0v\033[m')
time.sleep(0.5)
print(""""OPÇÕES DE TABUADA"
[1] Digitar um número 
[2] Computador Randozimar um número qualquer entre 0 a 10.""")
time.sleep(0.8)
opcao = int(input('Digite as opçoẽs: '))
if opcao == 1 :
    print('\033[36m_\033[m'*18)
    num = int(input('Digite o número: '))
    print('-'*20)
    for c in range(0,11):
        print(num , 'X' , c , '=' , num*c)
    print('-'*20)
elif opcao == 2 :
    #Randomizar um número inteiro
    computador = randint(0,10)
    print('-'*16)
    for c in range(0,11):
        print(computador , 'X' , c , '=' , computador*c)
    print('-'*16)
else:
    print('\033[31mOPÇÃO ERRADA!!!!\033[m')
