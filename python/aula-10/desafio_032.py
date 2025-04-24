a = int(input('ANO:'))
c = a % 4
d = a % 100
e = a % 400
if d > c == 0 or e == 0:
    print('É BISSEXTO!')
else:
    print('Não é BISSEXTO!')