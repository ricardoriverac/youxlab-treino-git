from random import randint
computador = randint (0,10)
contadorErros = 0
print ("\t_=_" * 20)
print ("Vou pensar em um número entre 0 e 10. Tente adivinhar... ")
print ("\t_=_" * 20)
jogador = int (input ('Em Qual número eu pensei ?? ' ))
while jogador != computador:
    print ("Você errou!!")
    jogador = int (input ('Em Qual número eu pensei ?? ' ))
    contadorErros += 1
print ("Você acertou !!, você pensou no número \033[31m{}\033[m".format(jogador))
print ("O computador pensou no número \033[32m{}\033[m !! ".format(computador))
print ("Você tentou \033[34m{}\033[m vezes até acertar.".format(contadorErros))
print ("-----FIM DE JOGO-----")