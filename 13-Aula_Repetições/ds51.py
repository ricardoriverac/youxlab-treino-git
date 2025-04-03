prm=int(input('Primeiro termo: '))
raz=int(input('Razão:  '))
dec=prm+(10 -1 ) * raz
for c in range(prm , dec + raz , raz):
    print('{}'.format(c), end=' ')
print('ACABOU')