import random

print ('VAMOS JOGAR PAR OU ÍMPAR! ')

vitorias = 0

while True:
    valorJogador = int(input('Digite um valor: '))
    escolhaJogador = str(input('Par ou Ímpar? [P/I] ')).upper()

    valorComputador = random.randint(1, 10)
    soma = valorJogador + valorComputador

    if soma % 2 == 0 and escolhaJogador == 'P' or soma % 2 != 0 and escolhaJogador == 'I':
        print (f'Você jogou {valorJogador} e o computador jogou {valorComputador}. O total é de {soma}. \nVocê GANHOU! \nVamos tentar novamente... ')
        vitorias += 1
    else:
        print (f'Você jogou {valorJogador} e o computador jogou {valorComputador}. O total é de {soma}. \nVocê PERDEU! ')
        break

print (f'Você ganhou {vitorias} vez(es)! ')