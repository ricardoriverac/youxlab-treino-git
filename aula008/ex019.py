from random import choice
alu1= (input('Primeiro aluno: '))
alu2=(input('Segundo alunlo: '))
alu3=(input('Terceiro aluno: '))
alu4= (input('aluno numero quatro: '))
lista = (alu1,alu2,alu3,alu4)

print('O aluno sorteado e {} '.format(choice(lista)))