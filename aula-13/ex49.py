numero = int(input('Digite o número que você quer a tabuada: '))
for n in range(1, 11):
    s = n * numero
    print('{} x {} = {}'.format(numero, n, s))
print('Essa é tabuada até 10 do número {}'.format(numero))