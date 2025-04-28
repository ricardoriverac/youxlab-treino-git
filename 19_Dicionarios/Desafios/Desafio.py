aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
for key, value in aluno.items():
	print(f'{key}:', value)