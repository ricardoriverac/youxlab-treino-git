from random import randint
computador= randint(0, 10)
print('Olá sou seu computador... pensei em um número entre 0 e 10.')
print('Consegue adivinhar?')
acertou= False
palpites= 0
while not acertou:
    jogador= int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('Um pouco mais...Tente novamente.')
        elif jogador > computador:
            print('Um pouco menos...tente novamente.')
print(f'Acertou com {palpites} tentativas!')