    
import random
jogosTotal = []
def sorteio(numJogos):
    for c in range(1, numJogos +1):
        for jogo in range(10):
            sorteio = random.randint(1, 60)
            jogosTotal.append(sorteio)
        print('-=' *30)
        print (f'Jogo {c} {jogosTotal}')
        jogosTotal.clear()
    print('-=' *30)

while True:  
    querJogar = str(input('Quer jogar na megasena? S/N: ')).upper()
    if querJogar == 'S':
        print('GERADOR DE PALPITE DA MEGA SENA')
        numJogos = int(input("Quantos jogos serão gerados? "))
        sorteio(numJogos)
    else:
        break




