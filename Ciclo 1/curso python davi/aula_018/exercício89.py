alunos = []
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
print("\nBoletim dos Alunos")
print("=" * 30)
print(f"{'No.':<4} {'Nome':<15} {'Média':>6}")
print("=" * 30)
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:<15} {aluno[2]:>6.1f}")
print("=" * 30)
while True:
    opc = float(input("Mostrar notas de qual aluno? (999 para sair): "))
    if opc == 999:
        break
    if 0 <= opc < len(alunos):
        print(f"Notas de {alunos[opc][0]}: {alunos[opc][1]}")
    else:
        print("Aluno não encontrado.")