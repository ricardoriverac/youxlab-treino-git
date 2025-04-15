import random
numeroComputador = random.randint(0, 5)
pergunta = int(input('Tente adivinhar o número que o computador escolheu entre 0 e 5 : '))
if pergunta == numeroComputador:
    print ('Você venceu! ')
else:
    print ('Você perdeu! ')    
print (f'O computador escolheu {numeroComputador} ') 