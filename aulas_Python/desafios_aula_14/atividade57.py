sexo = input('Infome seu sexo [F/M]')

while True:
    if sexo in 'Ff' or sexo in 'Mm':
        print(F'Sexo {sexo} registrado com sucesso!')

        break
    else:
        sexo = input('Dados incorretos. Digite seu sexo: ')
        
        