km = int(input('Digite a velocidade de um carro em Km: '))
multa = (km - 80)*7.00
if km >=80 :
    print('Vocẽ foi multado! Sua multa será de: {:.2f} reais! '.format(multa))
else :
    print('Ó')