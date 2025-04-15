import random

def par_ou_impar():
    vitorias = 0
    print("Vamos jogar Par ou Ímpar!")

    while True:
        jogador_escolha = ""
        while jogador_escolha not in ['P', 'I']:
            jogador_escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()

        try:
            jogador_numero = int(input("Escolha um número: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        computador_numero = random.randint(0, 10)
        total = jogador_numero + computador_numero
        resultado = "P" if total % 2 == 0 else "I"

        print(f"Você jogou {jogador_numero} e o computador {computador_numero}. Total: {total} -> {'PAR' if resultado == 'P' else 'ÍMPAR'}")

        if jogador_escolha == resultado:
            vitorias += 1
            print("Você VENCEU!\nVamos jogar novamente...\n")
        else:
            print("Você PERDEU!")
            break

    print(f"Fim de jogo! Você venceu {vitorias} vez(es) consecutivamente.")

par_ou_impar()
