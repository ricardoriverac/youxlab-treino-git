import random

a1 = str(input('aluno 1: '))
a2 = str(input('aluno 2: '))
a3 = str(input('aluno 3: '))
a4 = str(input('aluno 4: '))

a = [a1, a2, a3, a4]

escolhido = random.choice(a)

print('O aluno escolhido foi {}'.format(escolhido ))
