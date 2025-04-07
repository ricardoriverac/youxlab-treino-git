n =int(input('Digite um numero: '))
print('~'* 10)
t1=0
t2=1
print('~'*10)
print('{} -> {}'.format(t1 , t2), end =' ')
cont=3
while cont <= n:
    t3=t1 + t2
    print('-> {}'.format(t3), end =' ')
    t1 =t2
    t2=t3
    cont+=1
print('-> FIM')