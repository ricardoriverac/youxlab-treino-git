from random import randint
print('Vamos jogar jokenpô')
print('''Irei escolher entre pedra, papel e tesoura e você deve escolher a sua opção.
Escolha sua opção
[ 1 ] Pedra
[ 2 ] Tesoura 
[ 3 ] Papel''')

opcao=int(input('Sua opção: '))

eu=randint(0,3)

if opcao == 1 and eu == 2:
    print('Parabéns você ganhou, eu escolhi {}'.format(eu))

elif opcao == 1 and eu == 1:
    print('Empatamos, eu escolhi {}. Tente novamente'.format(eu))

elif opcao == 1 and eu == 3:
    print('Eu ganhei, eu escolhi {}. tente novamente'.format(eu))

elif opcao == 2 and eu == 1:
    print('Eu ganhei, eu escolhi {}. Tente novamente.'.format(eu))
elif opcao == 2 and eu == 2:
    print('Empatamos, eu escolhi {}, melhore.'.format(eu))

elif opcao == 2 and eu == 3:
    print('Parabéns, eu escolhi {}, infelizmente você ganhou'.format(eu))

elif opcao == 3 and eu == 1:
    print('Parabéns, eu escolhi {}, infelizmente você ganhou'.format(eu))

elif opcao == 3 and eu == 2:
    print('Eu ganhei. Escolhi {}, treine mais'.format(eu))

else: print('Empatamos, eu também escolhi {} que droga.'.format(eu))