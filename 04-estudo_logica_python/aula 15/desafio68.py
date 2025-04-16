import random
vitorias = 0
computador = True
while computador:
    jogador = str(input("Escolha: PAR ou IMPAR: ")).lower().strip()[0]
    numeroJogador = int(input('Digite um número: '))
    computador2 = random.randint(1, 10)
    soma = numeroJogador + computador2
    resultado = soma % 2
    if jogador == 'p':
        maquina = 'impar'
        if resultado == 0:
            print('Você ganhou!')
            vitorias += 1
            print(f'Você escolheu o número {numeroJogador} e o computador {computador2}')
            print(f'A soma desses números é {soma}')
            
        elif resultado == 1:
            print('Você perdeu! hahahaha')
            print(f'Você escolheu o número {numeroJogador} e o computador :{computador2}')
            print(f'A soma desses números é {soma}')
            
    if jogador == 'i':
        maquina2= 'par'
        if resultado == 1:
            print('Você ganhou!')
            vitorias += 1
            print(f'Você escolheu o número {numeroJogador} e o computador : {computador2}')
            print(f'A soma desses números é {soma}')
            
        if resultado == 0:
            print('Você perdeu! hahahha')
            print(f'Você escolheu o número {numeroJogador} e o computador :{computador2}')
            print(f'A soma desses números é {soma}')
            
    print(f'Você teve um total de {vitorias} vitórias')
    parar = str(input('Deseja continuar jogando? S/N:')).lower()
    if parar == 'n':
        break