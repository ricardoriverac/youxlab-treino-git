velocidade = float(input('velocidade de um carro: '))

if velocidade > 80:
    print('Ultrapassou os kms ')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia ')


