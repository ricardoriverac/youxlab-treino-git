carro= int(input('Qual era a velocidade do carro? '))
if carro > 80:
    n1=carro-80
    n2=n1*7
    print(f'Voce foi multado em {n2} reais e sua velocidade ultrapassou {n1} km/h acima do permitido')
else:
    print ('Voce esta na velocidade correta')
