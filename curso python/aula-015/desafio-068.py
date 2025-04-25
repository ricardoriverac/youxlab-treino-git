import random
vitorias = 0
par = ''
impar = ''
maquinaEsc = ''
isRodando = True
while isRodando:
    jogador = str(input("Escolha: PAR ou IMPAR: ")).lower().strip()[0]
    numeroJogado = int(input('Digite um número: '))
    numMaquina = random.randint(1, 10)
    soma = numeroJogado + numMaquina
    resultado = soma % 2
    if jogador == 'p':
        maquina = 'impar'
        if resultado == 0:
            print('Você venceu!')
            vitorias += 1
            print(f'Você escolheu o número {numeroJogado} e a maquina escolheu o número {numMaquina}')
            print(f'A soma desses números é {soma}')
            
        elif resultado == 1:
            print('Você perdeu!')
            print(f'Você escolheu o número {numeroJogado} e a maquina escolheu o número {numMaquina}')
            print(f'A soma desses números é {soma}')
            
    if jogador == 'i':
        maquina = 'par'
        if resultado == 1:
            print('Você venceu!')
            vitorias += 1
            print(f'Você escolheu o número {numeroJogado} e a maquina escolheu o número {numMaquina}')
            print(f'A soma desses números é {soma}')
            
        if resultado == 0:
            print('Você perdeu!')
            print(f'Você escolheu o número {numeroJogado} e a maquina escolheu o número {numMaquina}')
            print(f'A soma desses números é {soma}')
            
    print(f'Você teve um total de {vitorias} vitórias')
    para = str(input('Deseja continuar jogando? S/N:')).lower()
    if para == 'n':
        break
