import random
aleatorio = random.randint(0, 5)
escolhe = int(input('Qual número você acha que foi o sorteado? '))
if aleatorio == escolhe:
    print('PARABENS VOCÊ GANHOU!!!!')
else:
    print('Boa sorte na próxima!!!')
print('O número sorteado foi {}'.format(aleatorio))