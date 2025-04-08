c =1

while True:

    numero=int(input('Digite um número para ver a tabuada: '))
    print('<->'*10)

    if numero < 0:
            break

    for c in range(1,11): 
    
        print('{} X {} = {}'.format(numero,c,numero*c))

       


