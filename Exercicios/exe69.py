#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa
#cadastrada, o programa deverá perguntar se o usuario quer continuar. No final, mostre:

#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos.

pessoasMais18 = 0
homensCadastrados = 0
mulheresMenos20 = 0
pessoasCadastradas = 0

while True:
    print("\n---------------------------------------")
    print("-----------Cadastro de Pessoas---------")
    print("---------------------------------------\n")

    nome = input("Digite um nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome}: [F/M] ").upper()
    pessoasCadastradas += 1

    if sexo == "M":
        homensCadastrados += 1
    elif sexo == "F" and idade < 20:
        mulheresMenos20 += 1

    if idade >= 18:
        pessoasMais18 += 1
    
    pergunta = input("Você quer cadastrar mais pessoas? [S/N] ").upper()

    if pergunta == "N":
        print("Você finalizou o cadastro de pessoas.\n")

        print(f"Pessoas cadastradas: {pessoasCadastradas}.")
        print(f"Homens cadastrados: {homensCadastrados}.")
        print(f"Pessoas com +18: {pessoasMais18}")
        print(f"Mulheres com menos de 20 anos: {mulheresMenos20}.")
        break