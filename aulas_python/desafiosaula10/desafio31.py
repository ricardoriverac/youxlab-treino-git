distancia = int(input('Me diga a distância de uma viagem: '))
precoComDisconto = distancia * 0.45
precoSemDisconto = distancia * 0.50
if distancia <=200:
    print('O preço da passagem é {}'.format(precoSemDisconto))
else:
    print('O preço da passagem é {}'.format(precoComDisconto))
    
