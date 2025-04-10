
mf= ''
while True:
    mf=str(input('Digite seu sexo ''M/F:').upper())
    if mf in 'M':
        print('Você é um homem!')
    elif mf in 'F':
        print('você é uma mulher!' )
    else:
        print('Você digitou errado tente novamente ')
    break   