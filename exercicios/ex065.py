contador=0
media= 0
parar= ''
while parar != 'N':
    numero=int(input('Digite um valor: '))
    contador += 1
    media= contador / numero 
    parar= input('Deseja continuar? [Sim/Não]: ').upper() .capitalize()
if parar == 'N':
    print('Você digitou {} números...'.format(contador))
print('A média desses números é = {}'.format(media))