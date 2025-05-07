# Jogo do Dado

    # Jogador rola um dado (de 6 lados).
    # Tenta acertar o número que vai sair.

def cabecalho(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def linha():
    print("\n")

def placar(acertos, erros):
    linha()
    cabecalho("PLACAR FINAL")

    if acertos > 0:
        if acertos == 1:
            print("Você finalizou o jogo com 1 vitória")
        else:
            print(f"Você finalizou o jogo com {acertos} vitórias")

    if erros > 0:
        if erros == 1:
            print("Você finalizou o jogo com 1 derrota")
        else:
            print(f"Você finalizou o jogo com {erros} erros")
    linha()

import random
from time import sleep

acertos = 0
erros = 0

while True:
    linha()
    cabecalho("TESTE SUA SORTE")
    escolha = int(input("Escolha um lado do dado, de 1 a 6: "))

    if escolha < 1 or escolha > 6:
        print("Escolha inválida. Digite um número de 1 a 6.")
        continue

    sorteador = random.randint(1, 6)  # sorteando os lados do dado de 1 a 6

    print("Jogando o dado...")
    sleep(1)

    if escolha == sorteador:
        print("Jogador acertou o lado.")
        acertos += 1
    else:
        print("Jogador errou o lado.")
        erros += 1

    pergunta = input("Quer continuar?: [S/N] ").strip().upper()

    if pergunta not in ["S", "N"]:
        print("Resposta inválida.")
        placar(acertos, erros)
        break

    if pergunta == "N":
        print("Jogo encerrado")
        placar(acertos, erros)
        break