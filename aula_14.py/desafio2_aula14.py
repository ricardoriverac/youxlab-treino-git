from random import randint
palpites =0
acertou = False
computador = randint(0, 10)
print('Estou pensando num número... consegue adivinhar?')
while not acertou:
    jogador = int(input('Dê seu papite entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        print('Parabéns o computador pensou em {} e você pensou em {}.'.format(computador, jogador))
        acertou = True
else:
        print('Eu escolhi  {}.'.format(computador))
print('Foram necessárias {} tentativas para acertar.'.format(palpites))