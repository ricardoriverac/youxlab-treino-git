velocidade = int(input('Digite a sua velocidade'))
if velocidade >80:
     print('Você foi multado')
     multa = (velocidade-80) * 7
     print('Você foi multado em  R${}'.format(multa))
else:
    print('Você não foi multado')