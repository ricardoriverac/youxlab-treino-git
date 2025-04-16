from random import randint
import time

vitoria = 0
derrota = 0

while True:
    player = int(input("Diga um valor: "))
    pc = randint(0, 10)
    total = player + pc
    tipo = " "

    while tipo not in "PI":
        tipo = input("Par ou Ímpar? [P/I] ").strip().upper()[0]

    print(f"Você jogou {player} e o computador {pc}. Total de {total}")

    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("=-=-=-=" * 5)

    if (tipo == "P" and total % 2 == 0) or (tipo == "I" and total % 2 == 1):
        print("VOCÊ VENCEU!!")
        vitoria += 1
    else:
        print("VOCÊ PERDEU!!")
        derrota += 1

    print("=-=-=-=" * 5)

    while True:
        opcao = input("Vamos jogar novamente? [S/N]: ").strip().upper()[0]
        if opcao == "N":
            print(f"\nResultados Finais: Você ganhou {vitoria} e perdeu {derrota}.")
            exit()
        elif opcao == "S":
            print("Iniciando novamente...\n")
            time.sleep(1)
            break
        else:
            print("Dados inválidos. Tente novamente:")