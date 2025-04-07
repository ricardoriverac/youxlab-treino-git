import random
print('\033[1;34m---Tente adivinhar o numero que o computador está pensando (De 0 a 10)---\033[m')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

e = random.choice(numeros)


y = int(input('Qual o número que ele esta pensando? '))

while True:
    
    if y == e: 
        print('\033[1;32mVocê acertou!!\033[m')
        break

    else:
        y = int(input('\033[1;31mVocê errou, tente novamente:\033[m '))
    


