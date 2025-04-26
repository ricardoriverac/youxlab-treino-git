import random

computador= random.randint(1, 10)
numero= int(input('Palpite, um número de 1 a 10: '))

while numero != computador:
    if computador == numero:
        print('Você venceu!')
        if computador != numero:
            print('Você perdeu!')
        
    