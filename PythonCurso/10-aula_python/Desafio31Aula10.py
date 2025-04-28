distancia = float(input('Digite a distancia da sua viagem '))
mn = distancia * 0.50
m= distancia * 0.45

if distancia > 200:
    print('O valor da sua viagem é de R${:.2f}'.format(m))
else:
    print('O valor da sua viagem é de R${:.2f}'.format(mn))