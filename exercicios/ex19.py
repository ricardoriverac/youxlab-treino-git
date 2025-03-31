from random import choice
aluno1 = str (input ("Nome do primeiro aluno: "))
aluno2 = str (input ("Nome do segundo aluno: "))
aluno3 = str (input ("Nome do terceiro aluno: "))
aluno4 = str (input ("Nome do quarto aluno: "))
lista = (aluno1 , aluno2, aluno3 , aluno4)
sorteio = choice(lista)
print ("O aluno(a) escolhido(a) foi : {}".format(sorteio))
