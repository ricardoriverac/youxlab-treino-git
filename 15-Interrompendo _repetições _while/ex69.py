while True:

    idade = int(input('Idade de uma pessoa: '))

    sexo = ' '

    while sexo not in 'MF':

        sexo = str(input('Qual seu sexo? [F/M]: ')).strip().upper()[0]
    
    resp = ' '
    while resp not in "SN":

        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

print('Acabou')
