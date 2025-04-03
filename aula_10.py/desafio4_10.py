distancia = float(input('Digite qual foi a distancia da viagem: '))
abaixo = 0.50 * distancia
acima = 0.45 * distancia
if distancia < 200:
    print('A distancia foi abaixo de 200km, então você pagará {} '.format(abaixo))
else:
    print('A distancia foi acima de 200km, então você pagará {} '.format(acima))
distancia = float(input('Digite a distancia da viagem: '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Você vai pagar um valor de {}'.format(preco))  