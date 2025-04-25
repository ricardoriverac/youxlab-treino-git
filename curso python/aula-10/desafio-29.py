import random
velocidade = float(input('Qual a velocidade de um carro'))
print('O carro estava a {}km'.format(velocidade))
M = (velocidade-80)*7
if velocidade >= 80:
    print('Você foi mutado!')
    print('Você pagará R$7,00 por cada km excedente,')
    print('O valor ficará em R${}'.format(M))
else:
    print('siga em frente!')