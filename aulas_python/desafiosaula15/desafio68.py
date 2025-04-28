from random import randint
print('{}VAMOS JOGAR PAR OU ÍMPAR!{}'.format('\033[35m', '\033[m'))
par = impar = soma = vitorias = 0

while True:
    jogador = int(input('Qual número você escolhe? '))
    parOuImpar = input('Qual você escolhe, par ou ímpar?{}[P/I]:{} '.format('\033[33m', '\033[m')).upper()
    computador = randint(0, 10)
    soma = jogador+computador
    vitorias+=1
    
    if parOuImpar=='P' and soma%2==1 or parOuImpar=='I' and soma%2==0:
        print('{}COMPUTADOR VENCEU!{} '.format('\033[1;36m', '\033[m'))
        break
    
    elif parOuImpar=='P':
        print('Jogador escolheu PAR' )
        print('Computador escolheu ÍMPAR ')
    
    elif parOuImpar=='I':
        print('Jogador escolheu ÍMPAR ')
        print('Computador escolheu PAR ')
    print(f'Você escolheu o número {jogador}, computador escolheu o número {computador}')
    print('E a {}SOMA{} desses números é {}'.format('\033[35m', '\033[m', soma))
    print('{}JOGADOR VENCEU!{}'.format('\033[1;36m', '\033[m'))
    
print(f'Você escolheu o número {jogador}, computador escolheu o número {computador}')
print('E a {}SOMA{} desses números é {}'.format('\033[35m', '\033[m', soma))
print(f'Você teve {vitorias-1} vitórias!')
