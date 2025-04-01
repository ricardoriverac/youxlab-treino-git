import random
print('---Tente adivinhar o numero que o computador está pensando (De 0 a 10)---')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

e = random.choice(numeros)

y = int(input('Qual o número que ele esta pensando? '))

if y == (e): 
    print('Você acertou, parabens!')

else:
    print('Você errou, tente novamente..\n(O número que o computador estava pensando é {})'.format(e))