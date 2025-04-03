from random import randint
itens = ['pedra', 'papel', 'tesoura']
computador = randint (0,2)
print("""
[0]  Pedra
[1]  Papel
[2]  Tesoura
      """)
print ("\t_=_" * 20)
jogador = int (input ("Qual é a sua jogada: "))
# if jogador != 0 and jogador != 1 and jogador != 2:
#     print ("Jogada inválida!")
("VALENDOOOO")
print ("\t_=_" * 20)
print ("Compuador jogou: \033[33m{}\033[m ".format(itens[computador]))
print ("Jogador jogou: \033[33m{}\033[m ".format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print ("Empate")
    elif jogador == 1:
        print ("jogador ganha")
    elif jogador == 2:
        ("computador ganha")
elif computador == 1:
    if jogador == 1:
        print ("Empate")
    elif jogador == 2:
        print ("jogador ganha")
    elif jogador == 0:
        ("computador ganha")
elif computador == 2:
    if jogador == 2:
        print ("Empate")
    elif jogador == 1:
        print ("jogador ganha")
    elif jogador == 0:
        ("computador ganha")
        
print ("-----FIM DE JOGO-----")