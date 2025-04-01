import random
import math
nome1= str(input('Nome dos aluno (a): '))
nome2= str(input('Nome dos aluno (a): '))
nome3= str(input('Nome dos aluno (a): '))
nome4= str(input('Nome dos aluno (a): '))
lista= [nome1,nome2,nome3,nome4]
sorteio= random.choice(lista)
print('Aluno(a) escolhido(a) para apagar o quadro é: {} '.format(sorteio))