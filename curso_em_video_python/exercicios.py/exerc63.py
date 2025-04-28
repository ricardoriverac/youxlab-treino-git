t1 =0
t2 =1
t3 = t1 + t2
numero = int(input('Quantos termos você quer ver na sequência de Fibonacci? '))
valor = numero
cont = 3
print ('{} - {}'.format(t1, t2), end = ' ')
while cont <= numero:
    t3 = t1 + t2
    print(' - {}'.format(t3), end =' ')
    t1 = t2
    t2 = t3
    cont +=1
print ('\n\033[1;35mFIM')