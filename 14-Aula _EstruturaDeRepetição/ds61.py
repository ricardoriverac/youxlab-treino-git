prm=int(input('Primeiro termo: '))
raz=int(input('Razão:  '))
termo=prm
cont= 1
while cont <= 10:
    print('{}'.format(termo))
    termo +=raz
    cont += 1
print('fiiim')