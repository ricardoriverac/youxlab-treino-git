c =1
isRodando = True
while isRodando:

    numero=int(input('Digite um número para ver a tabuada: '))
    print('<->'*10)

    if numero <= 0:
        isRodando= False
    else:
        for c in range(1,11): 
        
            print('{} X {} = {}'.format(numero,c,numero*c))

       


