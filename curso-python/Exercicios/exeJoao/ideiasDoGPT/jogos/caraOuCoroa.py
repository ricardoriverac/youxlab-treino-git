# Cara ou Coroa

#     Jogador escolhe "cara" ou "coroa".
#     O computador sorteia o resultado.

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

import random
from time import sleep

vitorias = 0
derrotas = 0

while True:
    linha()
    cabecalho("TESTE SUA SORTE")
    pergunta = input("Cara ou Coroa? ").strip().lower()

    if pergunta not in ["cara", "coroa"]:
        print("Escolha inválida! Digite 'cara' ou 'coroa'.")
        continue

    sorteador = random.randint(0, 1)  # 0 = coroa, 1 = cara

    print("Sorteando...")
    sleep(1)

    if sorteador == 1:
        print("O computador sorteou: cara")
    else:
        print("O computador sorteou: coroa")

    if (pergunta == "cara" and sorteador == 1) or (pergunta == "coroa" and sorteador == 0):
        print("Jogador venceu.\n")
        vitorias += 1
    else:
        print("Jogador perdeu.\n")
        derrotas += 1

    pergunta2 = input("Quer continuar?: [S/N] ").strip().upper()

    if pergunta2 not in ["S", "N"]:
        print("Resposta inválida.")
        print("Jogo encerrado.")
        placar(vitorias, derrotas)
        break

    if pergunta2 == "N":
        print("Jogo encerrado.")
        placar(vitorias, derrotas)
        break
