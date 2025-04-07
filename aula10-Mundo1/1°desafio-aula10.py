#Jogo da adivinhação
from random import randint
computador=randint(0,5)#sorteia um n° de 1 à 5
player= input('Qual o númer que eu pensei?:')
if player==computador:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')