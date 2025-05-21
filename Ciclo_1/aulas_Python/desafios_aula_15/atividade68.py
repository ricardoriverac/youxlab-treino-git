from random import randint
print('\033[1;34m-=-=-=-=-= Jogo do Par ou Ímpar =-=-=-=-=-\033[m')
cont = 0
while True:
    imparOuPar = str(input('Você quer par ou impar? ')).upper()
    escolha = int(input('Certo, qual será seu número então? '))
    escolhapc = randint(0, 10)
    soma = escolhapc + escolha
    
    if imparOuPar == 'PAR': 
        if soma %2 == 0:
            print(f'\033[1;32m=-=-=-=-==-=-=-=-=\033[m\nVocê ganhou dessa vez! (O computador escolheu {escolhapc})\n\033[1;32m=-=-=-=-==-=-=-=-=\033[m')
            cont += 1
            continue
        else:
            print(f'\033[1;31m=-=-=-=-==-=-=-=-=\033[m\nVocê obteve uma sequência de {cont} vitorias\nObrigado por jogar, até mais..\n\033[1;31m=-=-=-=-==-=-=-=-=\033[m')
            break
        
    if imparOuPar == 'IMPAR': 
        if soma %2 == 1:
            print(f'\033[1;32m=-=-=-=-==-=-=-=-=\033[m\nVocê ganhou dessa vez! (O computador escolheu {escolhapc})\n\033[1;32m=-=-=-=-==-=-=-=-=\033[m')
            cont += 1
            continue
        else:
            print(f'\033[1;31m=-=-=-=-==-=-=-=-=\033[m\nVocê obteve uma sequência de {cont} vitorias\nObrigado por jogar, até mais..\n\033[1;31m=-=-=-=-==-=-=-=-=\033[m')
            break













# cont = 0
# par = 'PAR'
# impar = 'IMPAR'
# computador = random.choice(par, impar)

# import random
# while True:
#     jogada = str('Você quer par ou impar? ').upper().strip()
    
#     if computador != jogada:
#         cont += 1
        
#     else:
#         break
# print(f'Você acertou em {cont} tentativas, parabens!!')
    
    
