nome = input('Diga o nome da empresa: ')
km = int(input('A empresa cobra 2.50 por km rodado,quantos km deseja percorrer? '))
carro = int(input('Com nosso carro mais barato custanto 300 por dia,ficara com o carro quantos dias? '))
totalkm = km*2.50
totalcarro=300*carro
print('O total sera de {}'.format(totalkm + totalcarro))