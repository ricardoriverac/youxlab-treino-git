prm=int(input('Primeiro termo: '))
raz=int(input('Razão:  '))
termo=prm
cont= 1
mais=10
total=0
while mais != 0:
    total=total + mais
    while cont <= total:
        print('{} ->'.format(termo), end =' ')
        termo +=raz
        cont += 1
    print('PAUSA') 
    mais=int(input('Quantos numeros quer mostrar a mais ?  '))
print('FIM')