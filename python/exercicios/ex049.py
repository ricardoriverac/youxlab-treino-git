numero= int(input('Digite um número: '))
for count in range(0, 11):
    tabuada= numero * count
    print('{} x {}= {}'.format(numero, count, tabuada))