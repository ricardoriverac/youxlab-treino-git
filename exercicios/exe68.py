#Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido
#quando o jogador Perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

import random

vitorias = 0

while True:
    pergunta = input("Você deseja par ou impar? ").lower()
    jogador = int(input("Digite um número: "))
    computador = random.randint(0, 10)

    soma = jogador + computador
    print(f"\nA soma foi: {soma}")
    print(f"Computador : {computador}")
    print(f"Você: {jogador}\n")

    if soma % 2 == 0:
        print("Deu PAR.")
    else:
        print("Deu IMPAR.")

    if (soma % 2 == 0 and pergunta == "par") or (soma % 2 != 0 and pergunta == "impar"):
        print("Você venceu.\n")
        vitorias += 1
        perguntaFinal = input("Voce deseja continuar jogando: [S/N] ").upper()

        if perguntaFinal == "N":
            print("Voce encerrou o jogo.")
            print(f"Você finalizou o jogo com {vitorias} vitória(s).")
            break
        else:
            print("Voce continuou o jogo.")
    else:
        print("Você perdeu!\n")
        print(f"Você finalizou o jogo com {vitorias} vitória(s).")
        break
