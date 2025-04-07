import random
usuario = str(input('escolha pedra, papel ou tesoura: '))
lista = ['pedra','papel','tesoura']
computador = random.choice(lista)

print(f'''O computador escolheu {computador}
o jogador jogou {usuario}''')
if usuario == computador:
    print('O resultado foi um empate')
elif (
        (usuario == 'pedra' and computador == 'tesoura') or
        (usuario == 'papel' and computador == 'pedra') or
        (usuario == 'tesoura' and computador == 'papel')
    ):
        print("Você venceu!")
else:
    print("Você perdeu!")