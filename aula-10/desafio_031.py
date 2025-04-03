distancia = int(input('Qual a distância da viagem? '))
p1 = distancia * 0.50
p2 = distancia * 0.45
if distancia <=200:
    print('O preço da passagem ficará R${:.2f}' .format(p1))
else:
    print('O preço da passagem ficará R${:.2f}' .format(p2))