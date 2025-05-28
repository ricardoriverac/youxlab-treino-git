import random
sorteio = random.randint(1, 4)
aluno01 = str(input("nome do primeiro aluno "))
aluno02 = str(input("nome do segundo aluno "))
aluno03 = str(input("nome do terceiro aluno "))
aluno04 = str(input("nome do quarto aluno "))
aluno01 = aluno01
aluno02 = aluno02
aluno03 = aluno03
aluno04 = aluno04
if sorteio == 1:
    print("O aluno {}, foi escolhido".format(aluno01))
elif sorteio == 2:
    print("O aluno {}, foi escolhido".format(aluno02))
elif sorteio == 3:
    print("O aluno {}, foi escolhido".format(aluno03))
elif sorteio == 4:
    print("O aluno {}, foi escolhido".format(aluno04))
else: print("Aluno não sorteado.")