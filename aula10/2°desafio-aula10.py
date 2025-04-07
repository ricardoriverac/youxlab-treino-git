#Radar
velocidade=int(input('Qual a velocidade do carro?: '))
if velocidade > 80:
    print('Você foi multado!')
    multa=(velocidade-80)*7
    print('Você recebeu uma multa de {:.2f} reais'.format(multa))
else:
    print('Está tudo bem, tenha um bom dia!')