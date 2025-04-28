# from random import randint

# usuario = 1

# computador=randint(1,2)

# while usuario != computador:

#     usuario =int(input('Me diga o número que acha ser o certo: '))

#     if usuario < computador:
#         print('Faltou pouco,tente novamente...')

#     elif usuario > computador:
#         print('Diminua um puco o número...')

#     else:
#         print('Parabens você acertou! ')

from random import randint

computador =randint(0,10)

print('Sera que você adivinha o número? ')

acertou = False

palpites =0

while not acertou:

    jogador =int(input('Qual seu palpite: ')) 
        
    palpites +=1

    if jogador == computador:
        print('Mais...')

    elif jogador > computador:
        print('Menos...')
print('Parabens acertou!!! ')


