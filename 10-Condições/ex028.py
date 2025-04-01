import random
numeropc = random.randint(0, 5)

numero =  int(input('Adivinhe o número: '))

if numeropc >= 5:

    print('Voce Venceu ')

else:
    print('Voce perdeu')