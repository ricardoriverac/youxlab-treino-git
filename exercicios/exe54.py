#Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas
#pessoas ainda nao atingiram a maioridade e quantas ja são maiores

maiores = 0
menores = 0
anoAtual = 2025

for i in range(7):
    anoNascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade = anoAtual - anoNascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"\nPessoas maiores de idade: {maiores}")
print(f"Pessoas menores de idade: {menores}")


