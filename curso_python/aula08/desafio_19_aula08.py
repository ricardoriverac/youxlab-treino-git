import random
aluno1 = input ('Qual o nome do primeiro aluno? ')
aluno2 = input ('Qual o nome do segundo aluno? ')
aluno3 = input ('Qual o nome do terceiro aluno? ')
aluno4 = input ('Qual o nome do quarto aluno? ')
#nome = random.choice([aluno1, aluno2, aluno3, aluno4])
alunos = [aluno1, aluno2, aluno3, aluno4]

teste = random.choices(alunos, k=4)
print (f'O aluno escolhido é {teste}! ')