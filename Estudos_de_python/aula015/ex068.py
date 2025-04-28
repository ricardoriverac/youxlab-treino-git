from random import randint
valor=0
soma=0
vitoria=0
derrota=0

while True:


    parOuImpar=''

    computador=randint(1,20)

    print('<=>'*10)
    print(' ')

    print('VAMOS JOGAR PAR OU IMPAR!! ')

    print('<!>'*10)

    valor=int(input('Me diga um número: '))

    parOuImpar = str(input('Par ou Impar [P/I]: ')).upper()

    print('O valor que eu escolhi foi:{} '.format(computador))

    soma =(valor + computador)

    if valor == 0:
        break

    if soma % 2 == 0 and parOuImpar =='P' or soma % 2 != 0 and parOuImpar =='I':
            print(' ')
            print('A soma foi de {} '.format(soma))
            print('Você ganhou!! ')
            vitoria += 1

    else:
        print(' ')
        print('A soma foi de {} '.format(soma))
        print('Perdeu!!! ')
        derrota += 1

print('O programa terminou.Ao todo tivemos {} vitórias e {} derrotas: '.format(vitoria,derrota))



       



        











