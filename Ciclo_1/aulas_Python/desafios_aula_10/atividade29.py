v = float(input('Qual a velocidade que seu carro estava? '))

if v > 80:
   print('O limite de velocidade é 80km/h, Você foi multado')
   multa = (v - 80) * 7
   print('Você devera pagar uma multa de R${:.2f}'.format(multa))
    
    
else:
    print('Você não foi multado :)')