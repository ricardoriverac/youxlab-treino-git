import random

tentativa = 0
numeroComputador = random.randint(0, 11)

pergunta = int(input('Tente adivinhar o número que o computador escolheu entre 0 e 10 : '))

while pergunta != numeroComputador:
    pergunta = int(input('Você perdeu! Tente novamente: '))
    tentativa += 1

print (f'Você ganhou! Você precisou de {tentativa+1} tentativa(s). ')