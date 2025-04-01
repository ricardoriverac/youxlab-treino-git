nome = str(input('Digite seu nome!'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia {}!'.format (nome))

nome2 = str(input('Digite seu nome!'))
if nome2 == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Que nome feio que vpcê tem!')
print('Bom dia {}!'.format (nome2))

n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite sua segunda nota'))
s = (n1 + n2)/ 2
print('A média da sua nota foi {}'.format(s))

if s >= 6.0:
    print('Sua nota está acima da média')
else:
    print('Sua nota está abaixo da média')
