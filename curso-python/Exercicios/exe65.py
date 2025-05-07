#Crie um programa que leia varos números inteiros pelo teclado. No final da execução
#Mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
#O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores

numeros = []

while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    decisao = input("Você quer continuar digitando? [S/N] ").strip().upper()
    if decisao == "N":
        break

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"A média dos números digitados é {media}")
print(f"O maior número digitado é {maior}")
print(f"O menor número digitado é {menor}")
