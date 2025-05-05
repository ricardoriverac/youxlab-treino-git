
#QUANTAS PESSOAS SÃO MAIOR E QUANTAS MENOR DE IDADE
from datetime import date
atual=date.today().year
totalmaior=0
totalmenor=0
for contador in range(1,8):
    data=int(input(f'Digite a {contador}° data de nascimento:'))
    idade=atual-data
    if idade >= 18:
        totalmaior+=1
    else:
        totalmenor+=1
print(f'São {totalmaior} MAIOR de idade e {totalmenor} MENOR de idade ')