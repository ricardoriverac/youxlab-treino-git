import random
a1 = str(input('Qual o 1o aluno? '))
a2 = str(input('Qual o 2o aluno? '))
a3 = str(input('Qual o 3o aluno? '))
a4 = str(input('Qual o 4o aluno? '))
lista = [a1, a2, a3, a4]
sequencia = random.sample(lista, 4)
print('A sequência de alunos deve ser: {}'.format(sequencia))