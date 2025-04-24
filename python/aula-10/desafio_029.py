vel_m = int(input('Digite a velocidade atual do carro: '))
vel_r = 80
preço_m = (vel_m - vel_r) * 7  # Calculando o preço da multa

if vel_m <= vel_r:
    print('Você não foi multado! Continue sua viagem com segurança e tenha um bom dia!')
else:
    print('MULTADO!!! Você excedeu a velocidade máxima que é de 80km/h')
    print(f'Você deverá pagar R${preço_m:.2f}.')  # Exibindo o valor da multa de forma dinâmica
