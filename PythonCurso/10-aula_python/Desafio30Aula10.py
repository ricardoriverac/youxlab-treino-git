numero = int(input('Digite seu número'))
resultado = numero % 2
if resultado == 0:
    print('Seu número é {}, par'.format(numero))
else:
    print('Seu número é {}, ímpar'. format(numero))