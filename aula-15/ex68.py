from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR')
computador = randint(0,10)
soma = 0
venceu = 0
while True:
    print('-'*20)
    pi = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print('-'*20)
    valor = int(input('Diga um valor: '))
    soma = valor + computador
    if soma % 2 == 0:
        if pi == 'P':
            venceu += 1 
            print('VOCÊ VENCEU!')
            print(f'Você jogou {valor} e, o computador jogou {computador}, o total deu {soma}, deu par!')
        else:
            print('VOCÊ PERDEU!')
            print(f'Você jogou {valor} e, o computador jogou {computador}, o total deu {soma}, deu ímpar')
            #print(f'Jogo encerrado, você ganhou {venceu} partidas seguidas')
            break
    else:
        if pi == 'P':
            print('VOCÊ PERDEU!')
            print(f'Você jogou {valor} e o computador jogou {computador}, o total deu {soma}, deu ímpar')
            #print(f'Jogo encerrado, você ganhou {venceu} partidas consecutivas.')
            break
        else:
            venceu += 1
            print('VOCÊ VENCEU!')
            print(f'Você jogou {valor} e, o computador jogou {computador}, o total deu {soma}, deu par')
    print(f'Você venceu {venceu} vezes.')
print(f'Você ganhou {venceu} consecutivas!')