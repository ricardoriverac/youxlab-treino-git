aluno = {}
aluno['nome'] = input("Nome do aluno: ")
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")