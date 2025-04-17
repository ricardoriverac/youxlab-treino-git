#JOGO DA ADIVINHAÇÃO REMASTERIZADO
from random import randint
c = 0
computador= randint(0, 10)
print('Pensei em número de 1 à 10!\n Duvido você acertar!!')
while c >= 0:
    numero=int(input('Qual o seu chute?: '))
    c +=1
    print(computador)
    if numero == computador:
        print ("Você acertou!")
        break
    else:
        if numero != computador:
            if numero > computador:
                print('Menos ... Tente de novo!')
            elif numero < computador:
                print('Mais ... Tente de novo!')        
print(f'Você tentou {c} vezes.')
print('Fim!')
