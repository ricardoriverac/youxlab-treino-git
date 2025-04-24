def fatorial(num):
    valor =1
    for f in range(1, num+1):
        valor *= f
    return(valor)

def linha():
   print('~' * 40)
    
from time import sleep

linha()
sleep(0.5)
print('\033[3;35mVAMOS FATORAR UM NÚMERO\033[m'.center(50))
sleep(0.5)
linha()
sleep(0.5)

n = int(input('\033[1mDigite um número:\033[m '))
print(f'{n}! = {fatorial(n)}')
print(f'\033[3;35m[1]\033[1m Mostre o processo do cálculo do fatorial de {n}\033[m. ')
print(f'\033[3;35m[2]\033[1m Encerrar. \033[m')

def fatorial1 (num):
    valor = 1
    print(f'{num}! =', end=' ')
    for res in range(n, 0, -1):
     print(f'{res}', end = ' x ' if res > 1 else ' =  ') 

while True:
    resposta = int(input('\033[1mDigite sua resposta:\033[m [1/2] '))
    if resposta != 1 and resposta != 2:
        print('Opa, parece que você digitou errado, ', end ='')
    if resposta==1:
        fatorial1(n)
        break
    if resposta == 2:
        break

def fatorial1 (num):
    valor = 1
    print(f'{num}! =', end=' ')
    for res in range(n, 0, -1):
     print(f'{res}', end = ' x ' if res > 1 else ' = ' )
print('\n') 
    