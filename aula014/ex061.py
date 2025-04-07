print('Gerando uma PA parte 2: ')

primeiro=int(input('Me diga o valor do primeiro termo da PA: '))

razão=int(input('Diga a razão que sera trabalhado: '))


termo =primeiro

c  =1

while c <= 10:

    print('{} -'.format(termo),end ='') 

    termo += razão
    
    c += 1
print('FIM')