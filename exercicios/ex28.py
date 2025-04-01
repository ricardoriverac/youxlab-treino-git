from random import randint
computador = randint (0,5)
print ("\t_=_" * 20)
print ("Vou pensar em um número entre 0 e 5. Tente adivinhar... ")
print ("\t_=_" * 20)
jogador = int (input ('Em Qual número eu pensei ?? ' ))
if jogador == computador:
    print ("Você ACERTOUUU, o número que eu pensei foi : {}".format(computador))
else:
    print ("Você ERROUU!!")
    print ("O número escolhido foi: {}".format(computador))
    print ("Você escolheu o número: {}".format(jogador))
print ("-----FIM DE JOGO-----")