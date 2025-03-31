import random

n1 = str(input(' Aluno um'))
n2 = str(input(' Aluno dois'))
n3 = str(input(' Aluno três'))
n4 = str(input(' Aluno quatro'))


minha_lista = [n1, n2, n3, n4,]
random.shuffle(minha_lista)
print(' A ordem de apresentação será ')
print(minha_lista)
