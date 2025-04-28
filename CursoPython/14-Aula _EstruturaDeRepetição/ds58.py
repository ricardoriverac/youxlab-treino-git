from random import randint
computador =randint(0, 10)
print('>>>>'*20)
print('Ola!, sou seu computador ! vou pensar em um número')
print('<<<<'*20)
print('Sera que vocẽ consegue adivinhar? ')
print('>>>>'*20)
acertou = False
palpites= 0
while not acertou:
    jogador =int(input('Qual número você acha que é? '))
    palpites += 1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez!')
        elif jogador > computador: 
            print('Menos...Tente mais uma vez!')
print('Você acertou em {} tentativas .Parabens!'.format(palpites))


