#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:

#Quantos números foram digitados.
#A lista de valores, ordenada de forma decrescente.
#Se o valor 5 foi digitado e está ou não na lista.

lista = []
quantNum = 0

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    quantNum += 1
    decrescente = sorted(lista, reverse=True)

    pergunta = input("Você deseja continuar? [S/N] ").upper()
    if pergunta == "N":
        break
    elif pergunta not in ("N", "S"):
        print("\nResposta invalida!")
        print("Programa encerrado.\n")
        break
print(f"\nSua lista completa: {lista}")
print(f"Quantidade de números digitados: {quantNum}")
print(f"Números em ordem decrescente: {decrescente}")
if 5 in lista:
    print("O valor 5 ja foi digitado.\n")
else:
    print("O valor 5 não foi digitado.\n")
