registro = []

while True:
    nome = input("\nDigite o nome do(a) aluno: ")
    nota1 = float(input(f"Digite a nota 01, de {nome}: "))
    nota2 = float(input(f"Digite a nota 02, de {nome}: "))
    registro.append([nome, nota1, nota2])

    pergunta = input("Você deseja registrar, mais algum aluno? [S/N]: ").strip().upper()

    if pergunta == "N":
        print("Você encerrou o registro.")
        break

    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Registro finalizado.\n")
        break

print("\nBoletim dos alunos:")
print(f"{'No.':<4} {'Nome':<10} {'Média':>6}")
print("-" * 25)

for i, aluno in enumerate(registro):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i:<4} {aluno[0]:<10} {media:>6.1f}")

while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para sair): "))
    if opcao == 999:
        break
    if 0 <= opcao < len(registro):
        print(f"\nNotas de {registro[opcao][0]}: {registro[opcao][1]} e {registro[opcao][2]}")
    else:
        print("Número inválido.")