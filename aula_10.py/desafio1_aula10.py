from random import choice
print('Tente adivinhar qual número foi sorteado entre 0 e 5')
numero = [0, 1, 2, 3, 4, 5]
sorteio = choice(numero)
numero = int(input('Digite o número: '))
if numero == sorteio:
    print(f'Você acertou! Número: {sorteio}')
else:
    print('Número errado')
    print(f'O número que estava escondido era {sorteio}')