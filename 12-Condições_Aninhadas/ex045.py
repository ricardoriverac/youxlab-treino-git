import random

jogo = str(input('Pedra, Papel ou Tesoura?:')).lower()

opcoes = ['pedra', 'papel', 'tesoura']

esolhadopc = random.choice (opcoes)

if jogo == esolhadopc:
    print("Empate!")

elif jogo == "pedra":
    if esolhadopc == "tesoura":
        print("Você venceu!")
    else:
        print("Você perdeu!")

elif jogo == "papel":
    if esolhadopc == "tesoura":
        print("Você perdeu!")
    else:
        print("Você Venceu")
        
elif jogo == "pedra":
    if esolhadopc == "papel":
        print("Você Venceu")
    else:
        print("Você")