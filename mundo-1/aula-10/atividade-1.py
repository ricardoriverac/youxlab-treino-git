import random
numero = random.randint(0, 100)
nu2 = int(input("Adivinhe o número que estou pensando entre 0 e 5: "))
print('Voce acertou' if nu2 == numero else 'Tente de novo')


