velocidade = float(input('Digite a velocidade do carro km/h: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade. Você foi multado')
    multa = (velocidade - 80) * 7
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('Você não ultrapassou a velocidade permitida! Continue assim')