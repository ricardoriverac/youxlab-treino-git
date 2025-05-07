#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
#No final, mostre:

#Quantas pessoas foram cadastradas.
#Uma listagem com as pessoas mais pesadas.
#Uma listagem com as pessoas mais leves

pessoas = list()
maior = menor = 0 

while True:
    print("\nCadastro de pessoas")
    nome = input("Digite o nome da pessoa: ")
    peso = float(input(f"Digite o peso de {nome}: "))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    pergunta = input("Você deseja continuar cadastrando? [S/N] ").strip().upper()

    if pergunta == "N":
        break

    elif pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Programa encerrado.\n")
        break

print(f"\nForam cadastradas {len(pessoas)} pessoas.")

print(f"\nPessoas mais pesadas ({maior} kg):")
for p in pessoas:
    if p[1] == maior:
        print(f" - {p[0]}")

print(f"\nPessoas mais leves ({menor} kg):")
for p in pessoas:
    if p[1] == menor:
        print(f" - {p[0]}")

