numero = int(input('Digite um numero para ver sua tabuada: '))
for i in range(0,11):
    print('{} X {} = {}'.format(numero ,i,(numero * i)))