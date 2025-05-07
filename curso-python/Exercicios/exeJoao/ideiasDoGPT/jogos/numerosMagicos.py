# Jogo dos Números Mágicos

#     Escolha um número entre 1 e 100.
#     O jogo dá dicas tipo “maior” ou “menor”.

import random
from time import sleep

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

    if acertos == 1:
        print("Você finalizou o jogo com 1 vitória")
    elif acertos > 1:
        print(f"Você finalizou o jogo com {acertos} vitórias")

    if erros == 1:
        print("Você finalizou o jogo com 1 derrota")
    elif erros > 1:
        print(f"Você finalizou o jogo com {erros} derrotas")
    linha()

acertos = 0
erros = 0

while True:
    linha()
    cabecalho("NÚMERO MÁGICO")
    numeroSorteado = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            escolha = int(input("\nTente adivinhar o número de 1 a 100: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if escolha < 1 or escolha > 100:
            print("Número fora do intervalo. Tente entre 1 e 100.")
            continue

        tentativas += 1

        if escolha == numeroSorteado:
            print(f"Você acertou o número {numeroSorteado} em {tentativas} tentativa(s)!")
            acertos += 1
            break
        elif escolha < numeroSorteado:
            print("Dica: O número é MAIOR.\n")
        else:
            print("Dica: O número é MENOR.\n")

        if tentativas >= 10:
            print(f"Você excedeu o limite de tentativas. O número era {numeroSorteado}.")
            erros += 1
            break

    pergunta = input("Quer continuar? [S/N] ").strip().upper()

    if pergunta == "N":
        print("Jogo encerrado.")
        placar(acertos, erros)
        break
    elif pergunta != "S":
        print("Resposta inválida. Encerrando o jogo.")
        placar(acertos, erros)
        break
