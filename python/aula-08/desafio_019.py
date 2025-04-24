from random import choice
alunos = input('Escreva o nome dos alunos separados por vírgula: ').split(", ")
print('O aluno escolhido foi: {}'.format(choice(alunos)))