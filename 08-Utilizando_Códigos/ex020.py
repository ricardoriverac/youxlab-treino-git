import random

Nome1 = str(input('aluno 1: '))
Nome2 = str(input('aluno 2: '))
Nome3 = str(input('aluno 3: '))
Nome4 = str(input('aluno 4: '))

a = [Nome1, Nome2, Nome3, Nome4]

escolhido = random.shuffle (a)

print('A ordem de apresentação será: ')
print(a)