distancia=float(input(' digite sua distancia percorrida em km:'))
abaixo=0.50 * distancia
acima=0.45 * distancia
if distancia < 200 :
    print(' A distancia percorrida foi abaixo de 200km, entao vc pagarar {} '.format(abaixo))
else:
    print(' a distancia percorrida foi acima 200km,entao vc pagarar {} '.format( acima))
distancia=float(input( ' digite a distancia da viagem:'))
preco=distancia *0.50 if distancia<=200 else distancia* 0.45
print('voce vai pagar um valor de {}'.format(preco))