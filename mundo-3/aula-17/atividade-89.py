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

print("\n{:<4} {:<15} {:>6}".format("Nº", "Nome", "Média"))
print("-" * 30)
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:<15} {aluno[2]:>6.1f}")

while True:
    print("-" * 30)
    opc = int(input("Mostrar notas de qual aluno? (999 para sair): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if 0 <= opc < len(alunos):
        print(f"Notas de {alunos[opc][0]} são: {alunos[opc][1]}")
    else:
        print("Número inválido. Tente novamente.")
