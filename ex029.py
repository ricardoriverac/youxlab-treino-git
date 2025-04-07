velocidade=int (input('Informe a velocidade do carro: '))
if velocidade >80:
    print('MULTADO! Você excedeu o limite de 80Km/h')
    multa= velocidade * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    
print('Dirija com segurança. Tenha um ótimo dia!')