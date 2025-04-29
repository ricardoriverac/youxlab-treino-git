alunos = {

}
situacao = []
nom = alunos['nome'] = str(input("Nome do aluno: "))

gen = str(input(f'Qual o sexo de {nom} F/M: ')).upper()

me = alunos['média'] = float(input(f"Média: "))

if alunos['média'] < 7.0 and gen == 'F':

    alunos['Situação'] = 'Reprovada' 

elif alunos['média'] < 7.0 and gen == 'M':
    alunos['Situação:'] = 'Reprovado'
    
elif alunos['média'] > 7.0 and gen == 'F':
    alunos['Situação: '] = 'Aprovada'

elif alunos['média'] > 7.0 and gen == 'M':
    alunos['Situação'] = 'Aprovado'
print(alunos)