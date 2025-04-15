from random import randint
contagem = 0
print('Vamos jogar par ou ímpar')

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    resultado = 'PAR' if (jogador + computador) % 2 == 0 else 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} deu {resultado}.')
    if (opção == 'P' and resultado == 'PAR') or (opção == 'I' and resultado == 'ÍMPAR'):
        print('Você VENCEU!\nVamos jogar novamente...')
        contagem += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {contagem} vezes.')