#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

import random

sorteio = random.randint(1, 4)

nomeDoAluno01 = str(input("Qual é o nome do primeiro aluno? "))
nomeDoAluno02 = str(input("Qual é o nome do segundo aluno? "))
nomeDoAluno03 = str(input("Qual é o nome do terceiro aluno? " ))
nomeDoAluno04 = str(input("Qual é o nome do quarto aluno? "))

aluno01 = nomeDoAluno01
aluno02 = nomeDoAluno02
aluno03 = nomeDoAluno03
aluno04 = nomeDoAluno04

if sorteio == 1:
    print("O aluno {}, foi escolhido para apresentar!".format(aluno01))
elif sorteio == 2:
    print("O aluno {}, foi escolhido para apresentar!".format(aluno02))
elif sorteio == 3:
    print("O aluno {}, foi escolhido para apresentar!".format(aluno03))
elif sorteio == 4:
    print("O aluno {}, foi escolhido para apresentar!".format(aluno04))
else: print("Aluno não sorteado.")