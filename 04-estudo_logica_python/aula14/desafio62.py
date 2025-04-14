termo1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
numero=int(input(' quantos termos você quer:'))
dec = (termo1 + (numero-1)*razao)
contagem=termo1
 
while True :
    while contagem <= dec:
        print('{} -> '.format(contagem), end='')
        contagem += razao
    termo2= contagem
    continuar=str(input(' vc deseja continuar "s/n"'))
    if continuar in's':
        numero=int(input( 'Quantos termos ?'))
        dec = (termo2+ (numero-1)*razao)
        print('{} -> '.format(contagem), end='')
    else:
        print('fimmm')
        break
         
    

#while conta :
 #  =str(input(' vc deseja ver mais algum termo ''S/N').upper())
