distancia=int(input('Informe a distância em Km: '))
if distancia >200:
    passagem= distancia * 0.50
    print('Preço da passagem: {}'.format(passagem))
else:
    longas= distancia * 0.45 
    print('Preço da passagem: {} '.format(longas))