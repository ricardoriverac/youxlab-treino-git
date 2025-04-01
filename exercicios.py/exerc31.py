from time import sleep
distancia = float(input('Digite a distância de uma viagem em km: '))
print('Calculando o valor que deve ser pago...')
sleep(2)
if distancia <=200 :
    print('Você irá pagar {} reais pela viagem. '.format(distancia*0.50))
else :
    print('Você irá pagar {} reais pela viagem. '.format(distancia*0.45))
