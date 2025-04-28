dias=int(input('Quantos dias você ficou com o carro? '))
kmm=int(input('Quantos km você andou? '))
total= (dias*60) * (kmm * 0.15)
print('Então voce gastou {:.2f}'.format(total))