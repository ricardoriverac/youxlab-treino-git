num = int(input('Acerte o número:'))
if num != 5:
    print('Você errou! Tente novamente')
    num = int(input('Acerte o número:'))
    if num != 5:
        print('Você errou!')
    else:
        print('Você acertou!')
else:
    print('Você acertou!')
