n = int(input('Quantos termos quer? '))
a = 0
b = 1
c = 0
cont = 0
while cont < n:
    print('{}'.format(c), end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')