# Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
# Seu programa tem que análisar todos os valores e dizer qual deles é o maior.

todosNumeros = list()

while True:
    numero = int(input("Digite um número: "))
    todosNumeros.append(numero)
    pergunta = input("Deseja continuar? [S/N] ").strip().upper()

    if pergunta == "N":
        print("\nPrograma encerrdo.")
        break

    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Programa encerrado.\n")
        break

def maior(lista):
    if len(lista) == 0:
        print("\nNenhum número encontrado.\n")
    else:
        numMaior = max(lista)
        print(f"\nNúmeros digitados: {todosNumeros}\n")
        print(f"O maior número digitado é: {numMaior}\n")

maior(todosNumeros)