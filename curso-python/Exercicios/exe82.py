#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas lista extras que vão conter apenas valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteudo das tres listas geradas.

listaPrincipal = []
listaPar = []
listaImpar = []

while True:
    num = int(input("\nDigite um número: "))
    listaPrincipal.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

    pergunta = input("Você deseja continuar? [S/N] ").upper()
    if pergunta == "N":
        break

    if pergunta not in ("N", "S"):
        print("\nResposta invalida!")
        print("Programa encerrado.\n")
        break

print(f"\nLista Principal: {listaPrincipal}")
print(f"Lista Par: {listaPar}")
print(f"Lista Impar: {listaImpar}\n")

