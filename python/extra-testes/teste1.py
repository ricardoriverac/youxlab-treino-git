import random as rd
from time import sleep

valores = {'Ás' : 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7' : 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Dama': 12, 'Rei': 13}
print('Vamos jogar cartas. Irei sortear uma carta para você e uma para mim, quem tirar a maior ganha.')

while True:
    jogador = rd.choice(list(valores.keys()))
    computador = rd.choice(list(valores.keys()))
    print(f'Eu tirei {computador} e você tirou {jogador}')
    sleep(1)
    if valores[jogador] > valores[computador]:
        print('Parabéns! Você venceu.')
    elif valores[jogador] == valores[computador]:
        print('VISH, pelo visto empatamos')
    else:
        print('Infelizmente não deu para você, eu GANHEI!')
    resposta = str(input('Deseja continuar [s/n]? ')).lower()[0]
    if resposta == 'n':
        break
    sleep(1)