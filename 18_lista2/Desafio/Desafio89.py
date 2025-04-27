import time

boletim = []

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    while True:
        opcao = input("Deseja continuar? [S/N]: ").upper().strip()
        if opcao not in ["S", "N"]:
            print("Erro. Tente novamente com S ou N.")
        else:
            break

    if opcao == "N":
        print("Gerando resultados...")
        time.sleep(2)
        print("__" * 30)
        print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
        print("-" * 30)
        for i, a in enumerate(boletim):
            print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
        break