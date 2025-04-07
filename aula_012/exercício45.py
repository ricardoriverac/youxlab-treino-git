from random import randint
itens = ("pedra', 'papel', 'tesoura")
pc = randint(0 , 2)
print (''' opções
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura ''')
jgd = int(input('qual a sua jogada? '))
print ('-=' * 11)
print ('a máquina jogou {}'.format(itens[pc]))
print ('o jogador jogou {}' .format(itens[jgd]))
print ('-=' * 11)
if pc == 0: #a máquina jogou pedra
    if jgd == 0:
        print('empatou. ')
elif jgd == 1:
    print('jogador ganhou. ')
elif jgd == 2:
    print('maquina ganhou. ')
elif pc == 1:#a maquina jogou papel
    if jgd == 0:
        print('maquina venceu. ')
elif jgd == 1:
    print('empatou. ')
elif jgd == 2:
    print(' jogador ganhou. ')
elif pc == 2:#computador jogou tesoura
    if jgd == 0:
        print('jogador ganhou.')
elif jgd == 1:
    print('maquina ganhou. ')
elif jgd == 2:
    print('empatou. ')
else:
    print('jogada inválida. ')