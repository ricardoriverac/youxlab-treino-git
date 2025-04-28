from random import shuffle
al1 = input('Fale o nome de um aluno:')
al2 = input('Fale o nome de outro aluno:')
al3 = input('Fale o nome de outro:')
al4 = input('Fale o nome do quarto aluno:')
alunos = [al1, al2, al3, al4]
shuffle(alunos)

print('A ordem sorteada foi ')
print(alunos)      
