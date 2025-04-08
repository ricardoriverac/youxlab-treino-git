aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media: '))
print(f'Nome é igual a {aluno["Nome"]}')
print(f'A media é igual a {aluno["Media"]}')
if aluno['Media'] > 5 :
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')