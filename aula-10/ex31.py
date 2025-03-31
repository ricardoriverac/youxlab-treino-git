distancia=float(input('Quantos quilometros tem a distancia da sua viagem? '))
if distancia>200:
    passsagem=distancia*0.45
    print('Sua passagem custará R${}'.format(passsagem))
else:
    passsagem=distancia*0.50
    print('Sua passagem custará R${}'.format(passsagem))