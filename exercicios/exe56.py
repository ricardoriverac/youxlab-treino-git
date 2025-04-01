#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A media de idade do grupo
#Qual e o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos

somaIdades = 0
idadeHomensMaisVelhos = 0
homemMaisVelho = ""
mulheresMenos20 = 0

for j in range(4):
    nome = input(f"Digite o nome da {j+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (F/M): ").strip().upper()

    somaIdades += idade

    if sexo == "M" and idade > idadeHomensMaisVelhos:
        idadeHomensMaisVelhos = idade
        homemMaisVelho = nome

    if sexo == "F" and idade < 20:
        mulheresMenos20 += 1

mediaDeIdades = idade / 4

print("\nResultados:")
print(f"A média de idade do grupo é {mediaDeIdades:.1f} anos.")
if homemMaisVelho:
    print(f"O homem mais velho é {homemMaisVelho} com {idadeHomensMaisVelhos} anos.")
else:
    print("Não há homens no grupo.")
print(f"Há {mulheresMenos20} mulher(es) com menos de 20 anos.")