# Faça um mini-sistema que ultiliza o interactive Help do python.
# O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario
# Digitar a palavra "FIM", o programa se encerrará

from time import sleep
c = ("\033[m",           # 0 - sem cores
       "\033[0;30;41m]",   # 1 - vermelho
       "\033[0;30;42m]",   # 2 - verde
       "\033[0;30;43m]",   # 3 - amarelo
       "\033[0;30;44m]",   # 4 - azul
       "\033[0;30;45m]",   # 5 - roxo
       "\033[7;30m]",);    # 6 - branco

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'", 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")
    sleep(2)


def titulo(mensagem, cor=0):
    largura = len(mensagem) + 8
    print(c[cor], end="")
    print("~" * largura)
    print(f"{mensagem.center(largura)}")
    print("~" * largura)
    print(c[0], end="")
    sleep(2)

comando = ""
while    True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = input("Função ou Biblioteca -> ")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)