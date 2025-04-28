from time import sleep
km = int(input('Digite a velocidade de um carro em Km: '))
multa = (km - 80)*7.00
print('VERIFICANDO SE SERÁ MULTADO...')
sleep(2)
if km >=80 :
    print('{}Km? Vocẽ foi multado! Sua multa será de: {:.2f} reais! '.format(km, multa))
else :
    print('Ótimo, {}Km está razoável. Você não receberá multa. '.format(km))

