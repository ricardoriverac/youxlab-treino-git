km = int(input('Diga a velocidade de um carro: '))
kmCusto = (km - 80) * 7
if km > 80:
    print('Você foi mutado, sua velocidade está acima do limite, que é 80km/h!')
    print('Você vai ter que pagar uma multa de {}'.format(kmCusto))
else:
    print('Você está na velocidade adequada, parabéns! ')
