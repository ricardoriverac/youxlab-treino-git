numero= int(input('Digite um número aqui: '))
for a in range(0): 
    if numero % numero == 0 or numero % 1== 0:
     print('{} é um número primo!'.format(numero))
else:
    print('{} não é um número primo!'.format(numero))