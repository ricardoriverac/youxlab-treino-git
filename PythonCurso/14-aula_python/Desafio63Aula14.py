n1 = int(input('Quantos termos você quer mostrar? '))
t =0
t2 =1
print('{}  {} '.format(t,t2), end='')
cont = 3
while cont <= n1:
    t3 = t + t2
    print('{} '.format(t3), end='')
    t = t2
    t2 = t3
    cont += 1


print('FIMMMM')
 
