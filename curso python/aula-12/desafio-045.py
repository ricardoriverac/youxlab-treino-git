import random

def jogar_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    escolha_jogador = int(input("Digite o número da sua escolha: ")) - 1

    if escolha_jogador not in [0, 1, 2]:
        print("Escolha inválida! Tente novamente.")
        return

    escolha_computador = random.randint(0, 2)

    print(f"\nVocê escolheu: {opcoes[escolha_jogador]}")
    print(f"O computador escolheu: {opcoes[escolha_computador]}\n")

    # Verifica o vencedor
    if escolha_jogador == escolha_computador:
        print("Empate! 🤝")
    elif (escolha_jogador == 0 and escolha_computador == 2) or \
         (escolha_jogador == 1 and escolha_computador == 0) or \
         (escolha_jogador == 2 and escolha_computador == 1):
        print("Você venceu! 🎉")
    else:
        print("O computador venceu! 😢")

# Chama o jogo
jogar_jokenpo()

