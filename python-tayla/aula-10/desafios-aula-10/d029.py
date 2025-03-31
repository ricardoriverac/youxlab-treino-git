velocidade = int(input('A qual velocidade você estava? '))
multa = (velocidade-80)*7
if velocidade > 80:
    print(f'Você foi multado! O valor da sua multa é R${multa}')
else:
    print('Você não foi multado, PARABÉNS!')
