numero = int(input('Digite um número para ver a tabuada dele: '))
for multiplo in range(0, 11):
    resultado = (numero * multiplo)
    print('{} * {} = {}'.format(numero, multiplo, resultado))
