import random
numero = random.randint(0, 5)
text = int(input('Adivinhe o número que estou pensando entre 0 e 5: '))
print('você acertou!' if text == numero else 'tente de novo')