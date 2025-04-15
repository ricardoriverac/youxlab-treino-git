distancia = int (input('qual é a distância da sua viagem? '))
viagemCurta = distancia * 0.5
viagemLonga = distancia * 0.45
if distancia < 201:
    print (f'O preço da sua passagem é de R${viagemCurta} ')
else:
    print (f'O preço da sua passagem é de R${viagemLonga} ')  