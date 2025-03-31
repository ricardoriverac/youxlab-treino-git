velocidade=float(input('Você estava dirigindo a qual velocidade? '))
if velocidade>80:
    print('Você foi multado. Você passou do limite do 80km/h')
    multa = (velocidade-80)*7
    print('Sua multa é de {:.2f} R$'.format(multa))
else:
    print('Parabéns, você é um motorista consciente!!')