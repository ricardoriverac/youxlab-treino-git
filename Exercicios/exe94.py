#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa
#Em um discionario e todos os discionarios em uma lista. No final, mostre:
#A - Quantas pessoas foram cadastradas
#B - A média de idade do grupo
#C - Uma lista com todas as mulheres
#D - Uma lista com todas as pessoas com idade acima da média

caixaDeInfo = dict()
listaDeInfo = list()
nomesDeMulheres = list()
somaIdade = 0
quantPessoas = 0
media = 0

while True:
    caixaDeInfo.clear()

    nome = input("Digite um nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome}: [F/M] ").upper()
    quantPessoas += 1
    somaIdade += idade
    pergunta = input("Você deseja cadastrar outra pessoa? [S/N] ").upper()

    caixaDeInfo["nome"] = nome
    caixaDeInfo["idade"] = idade
    caixaDeInfo["sexo"] = sexo

    if sexo == "F":
        nomesDeMulheres.append(nome)

    if sexo == "F":
        caixaDeInfo["sexo"] = "Feminino"
    elif sexo == "M":
        caixaDeInfo["sexo"] = "Masculino"  

    listaDeInfo.append(caixaDeInfo.copy())

    if pergunta == "N":
        print(f"\nPrograma encerrado.\n")
        break

    if pergunta not in ["S", "N"]:
        print(f"\nResposta inválida.")
        print("Programa encerrado.\n")
        break

    if sexo not in ["F", "M"]:
        print(f"\nResposta inválida.")
        print("Programa encerrado.\n")
        break

media = somaIdade / quantPessoas
print(f"Foram cadastradas {quantPessoas} pessoas.")
print(f"A média de idade é {media:.2f}.")

print("\nLista de mulheres cadastradas:")
print(nomesDeMulheres)

print("\n")
print("Pessoas com idade acima da média:")
for pessoa in listaDeInfo:
    if pessoa["idade"] > media:
        print(f"{pessoa['nome']} com {pessoa['idade']} anos.")