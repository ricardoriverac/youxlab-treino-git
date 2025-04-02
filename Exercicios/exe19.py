#Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

num = random.randint(1, 4)

aluno01 = "João"
aluno02 = "Fabio"
aluno03 = "Lucas"
aluno04 = "Bryan"

if num == 1:
    print("Aluno {}, foi escolhido para apagar o quadro.".format(aluno01))
elif num == 2:
    print("Aluno {}, foi escolhido para apagar o quadro.".format(aluno02))
elif num == 3:
    print("Aluno {}, foi escolhido para apagar o quadro.".format(aluno03))
elif num == 4:
    print("Aluno {}, foi escolhido para apagar o quadro.".format(aluno04))
else: print("Nenhum aluno foi escolhido.")