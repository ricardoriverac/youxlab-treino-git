numero = int(input('Digite um numero para ver sua tabuada: '))
for c in range(0,11):
    print('{} X {} = {}'.format(numero ,c,(numero * c)))