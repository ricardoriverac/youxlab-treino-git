from random import shuffle
alu1= (input('Primeiro aluno: '))
alu2=(input('Segundo alunlo: '))
alu3=(input('Terceiro aluno: '))
alu4= (input('aluno numero quatro: '))
lista = [alu1,alu2,alu3,alu4]
shuffle(lista)
print('A nova ordem sera: ')
print(lista)