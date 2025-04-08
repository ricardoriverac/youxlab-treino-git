print('Gerando uma PA parte 2: ')

primeiro=int(input('Me diga o valor do primeiro termo da PA: '))

razão=int(input('Diga a razão que sera trabalhado: '))


termo =primeiro
repeticao = 10

c  =1
isRodando = True
while isRodando != False:
    while c <= repeticao :

        print('{} -'.format(termo),end ='') 

        termo += razão
        
        c += 1

    print('Pausa ')
    mais =str(input('Você quer rodar denovo? [S/N] '.upper()))
    if mais == 'N':

        isRodando = False
        
    else:
        repeticao =int(input('Quantos termos deseja mostrar a mais? '))
        c = 1