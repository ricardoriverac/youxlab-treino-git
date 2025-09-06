aluno = dict()
aluno['nome'] = input("Nome do aluno: ")
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print("\nResultado:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")