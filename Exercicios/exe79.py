#Crie um programa onde o usuario possa digitar varios valores e numeros
#e cadastra-los em uma lista. Caso o número ja exista la dentro, ele não será adicionado.
#No final, serão exibidos todos os valores unicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input("Digite um número: "))

    if num not in lista:
        lista.append(num)
    else:
        print("Já existe!")

    pergunta = input("Você deseja continuar digitando? [S/N] ").upper()
    if pergunta == "N":
        break
    
print("\nVocê encerrou o programa.")
print(f"Esta é sua tabela em ordem crescente: {sorted(lista)}")

