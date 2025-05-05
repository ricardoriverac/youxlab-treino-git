#DICIONÁRIO EM PYTHON
aluno={}
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Média do({aluno["nome"]}: '))
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
if aluno['media']>=7.0:
    print('Situação igual a Aprovado')
elif aluno['media']>=5.0 and aluno['media']<7.0:
    print('Situação igual a Recuperação')
else:
    print('Situação igual a Reprovado')
