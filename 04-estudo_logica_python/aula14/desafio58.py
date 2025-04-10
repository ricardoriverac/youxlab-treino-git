from random import randint
from time import sleep
palpites = 0
acertou = False
print('Estou pensando num número... consegue adivinhar?')
while not acertou:
    comp = randint(0, 10)
    jogador = int(input('Dê seu papite entre 0 e 10: '))
    palpites += 1
    if jogador == comp:
        print('Parabéns o computador pensou em {} e você pensou em {}.'.format(comp, jogador))
        acertou = True
else:
        print('Quase.. pensei em {}.'.format(comp))
print('Foram necessárias {} tentativas para acertar.'.format(palpites))