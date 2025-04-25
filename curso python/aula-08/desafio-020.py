#faça um programa onde os quatro alunos vão apresentar um trabalho e o programa mostre a ordem de apreesentação 

import random
aluno1 = str(input('qual o nome do primeiro aluno'))
aluno2 = str(input('qual o nome do segundo aluno?'))
aluno3 = str(input('qual o nome do terceiro aluno?'))
aluno4 = str(input('qual o quarto aluno?'))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)



print('a ordem de apresentação será:')
print(lista)


