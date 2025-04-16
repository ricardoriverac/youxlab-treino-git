# Par ou Ímpar

#     O jogador escolhe par ou ímpar e um número.

#     O computador escolhe outro número.

#     Soma os dois e verifica se o jogador venceu.

import random
from time import sleep

def cabecalho(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def linha():
    print("\n")

def placar(vitorias, derrotas):
    linha()
    cabecalho("PLACAR FINAL")

    if vitorias > 0:
        if vitorias == 1:
            print("Você finalizou o jogo com 1 vitória")
        else:
            print(f"Você finalizou o jogo com {vitorias} vitórias")

    if derrotas > 0:
        if derrotas == 1:
            print("Você finalizou o jogo com 1 derrota")
        else:
            print(f"Você finalizou o jogo com {derrotas} derrotas")
    
    linha()

soma = 0
vitorias = 0
derrotas = 0

while True:
    linha()
    cabecalho("TESTE SUA SORTE")
    pergunta = input("Par ou Ímpar? ").strip().lower()

    if pergunta == "par":
        jogador = int(input("Digite um número par: "))
        sleep(0.5)
        print("Esperando o outro jogador...")
        sleep(1.5)    
        if jogador % 2 != 0:
            print(f"\nERRO! O número {jogador} não é par.\n")
            continue

    elif pergunta == "impar":
        jogador = int(input("Digite um número ímpar: "))
        sleep(0.5)
        print("Esperando o outro jogador...")
        sleep(1.5)
        if jogador % 2 == 0:
            print(f"\nERRO! O número {jogador} não é ímpar.\n")
            continue
    else:
        print("\nOpção inválida! Escolha 'par' ou 'impar'.\n")
        continue

    print(f"\nVocê escolheu o número: {jogador}")
    computador = random.randint(0, 10)
    print(f"O Computador escolheu o número: {computador}")
    soma = jogador + computador
    print(f"A soma dos dois números é: {soma}\n")

    if (pergunta == "par" and soma % 2 == 0) or (pergunta == "impar" and soma % 2 != 0):
        print("Jogador ganhou!\n")
        vitorias += 1
    else:
        print("Jogador perdeu.\n")
        derrotas += 1

    pergunta2 = input("Quer continuar jogando? [S/N]: ").strip().upper()

    if pergunta2 not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Programa encerrado.\n")
        placar(vitorias, derrotas)
        break

    if pergunta2 == "N":
        print("\nPrograma encerrado.\n")
        placar(vitorias, derrotas)
        break
