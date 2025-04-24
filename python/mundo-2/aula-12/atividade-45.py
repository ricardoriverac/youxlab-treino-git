import random
usuario = str(input(''))

lista = ['pedra', 'papel', 'tesoura']

computador = random.choice(lista)


print(f'''O computador esolheu {computador}
o jogador escolheu {usuario}''')
if usuario == computador:
    if usuario == computador:
        print("Empate!")
elif (
        (usuario == 'pedra' and computador == 'tesoura') or
        (usuario == 'papel' and computador == 'pedra') or
        (usuario == 'tesoura' and computador == 'papel')
):
    print('Voce perdeu')
else:
    print('Voce perdeu')