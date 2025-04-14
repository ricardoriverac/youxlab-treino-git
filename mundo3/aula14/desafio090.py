aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip().capitalize()
aluno['media'] = float(input('média: '))

print('-' * 65)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')

if aluno["media"] < 7 and aluno["media"] >= 5:
    print(f'- Com média {aluno["media"]}, o(a) aluno(a) {aluno["nome"]} está em RECUPERAÇÃO!')
elif aluno["media"] >= 7:
    print(f'- Com média {aluno["media"]}, o(a) aluno(a) {aluno["nome"]} está APROVADO(A)!')
else:
    print(f'- Com média {aluno["media"]}, o(a) aluno(a) {aluno["nome"]} está REPROVADO(A)!')
print('-' * 65)
