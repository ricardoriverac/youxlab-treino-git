tot18 = totH = totM20 = 0
while True:

    idade = int(input('Idade de uma pessoa: '))

    sexo = ' '

    while sexo not in 'MF':

        sexo = str(input('Qual seu sexo? [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totH += 1
    if sexo == 'F':
        totM20 += 1

    resp = ' '
    while resp not in "SN":

        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':  
        break
print(f'O total de pessoas com mais de 18 anos é: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')

