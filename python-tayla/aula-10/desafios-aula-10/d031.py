distancia = int(input('Qual é a distância da sua viagem? '))
valor1 = distancia * 0.5
valor2 = distancia * 0.45
if distancia <= 200:
    print(f'O valor da sua viagem é de R${valor1}')
if distancia > 200:
    print(f'O valor da sua viagem é de R${valor2}')