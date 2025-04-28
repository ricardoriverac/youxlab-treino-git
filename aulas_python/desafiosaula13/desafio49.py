numero = int(input('Digite um número: '))
print('A tabuada desse número é: ')
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, c*numero))
    