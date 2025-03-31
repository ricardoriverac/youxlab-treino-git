#Jogo de pedra, papel ou tesoura

import random

sorteio = random.randint(0, 2)

print("Escolha: ")
print("[ 0 ] Pedra")
print("[ 1 ] Papel")
print("[ 2 ] Tesoura")

decisao = input("Qual será sua jogada? ")

if decisao not in ["0", "1", "2"]:
    print("Escolha inválida! Tente novamente.")
else:
    decisao = int(decisao)

    print("\nVocê escolheu: {}".format(decisao))
    print("O computador escolheu: {}\n".format(sorteio))

if decisao == sorteio:
        print("Empate!")
elif (decisao == 0 and sorteio == 2) or (decisao == 1 and sorteio == 0) or (decisao == 2 and sorteio == 1):
    print("Você venceu!")
else:
    print("Você perdeu!")
