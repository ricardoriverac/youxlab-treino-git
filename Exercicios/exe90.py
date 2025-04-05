#Faça um programa que leia nome e média de um aluno.
#Guardando tambem a situação em um dicionario. No final, mostre o conteudo da estrutura na tela.

registro = []

while True:
    nome = input("\nDigite o nome do(a) aluno: ")
    nota1 = float(input(f"Digite a nota 01, de {nome}: "))
    nota2 = float(input(f"Digite a nota 02, de {nome}: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "situacao": situacao
    }

    registro.append(aluno)

    pergunta = input("Você deseja registrar, mais algum aluno? [S/N]: ").strip().upper()
    if pergunta == "N":
        print("Você encerrou o registro.")
        break
    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Registro finalizado.\n")
        break

print("\nBoletim dos alunos:")
print(f"{'No.':<4} {'Nome':<10} {'Média':>6} {'Situação':>12}")
print("-" * 35)

for i, aluno in enumerate(registro):
    print(f"{i:<4} {aluno['nome']:<10} {aluno['media']:>6.1f} {aluno['situacao']:>12}")

while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para sair): "))
    if opcao == 999:
        break
    if 0 <= opcao < len(registro):
        aluno = registro[opcao]
        print(f"Notas de {aluno['nome']}: {aluno['nota1']} e {aluno['nota2']}")
        print(f"Situação de {aluno['nome']}: {aluno['situacao']}")
    else:
        print("Número inválido.")
