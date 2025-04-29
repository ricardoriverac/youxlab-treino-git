#tempo = int(input('Quantos anos tem seu carro? '))

#if tempo <=3: 
    #print('Carro novo')
#else:
    #print('carro velho')
#print('--FIM--')

#tempo = int(input('Quantos anos tem seu carro? '))
#print('Carro novo'if tempo<=3 else'Carro velho')
#print('--FIM--')

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2)/2
print('Sua méda foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS: ')
else:
    print('Sua média foi ruim! Estude MAIS')