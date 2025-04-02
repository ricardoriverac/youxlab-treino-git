#Ordem de apresetações
import random
aluno1= str(input('Nome do 1° aluno:'))
aluno2= str(input('Nome do 1° aluno:'))
aluno3= str(input('Nome do 1° aluno:'))
aluno4= str(input('Nome do 1° aluno:'))
lista=[aluno1,aluno2,aluno3,aluno4]
sorteio=random.shuffle(lista)#shuffle -->função que embaralha
print('A ordem será:')
print(lista)