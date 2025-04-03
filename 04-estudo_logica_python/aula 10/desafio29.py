velocidade= float(input(' Qual a velocidade do carro km/h:'))
if velocidade > 80:
    print ('Você ultrapassou o limite de velocidade.Você serar multado')
    multa= (velocidade-80)* 7
    print('Sua multa serar R$:{:.2f}'.format(multa))
else:
    print('Voce nao ultrapassoua velocidade permetida! Continua assim !')