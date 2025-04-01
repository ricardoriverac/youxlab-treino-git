km =float(input('Que distancia voce percorreu?  '))
prc= km * 0,50
lng= km * 0,45
if km >200:
    print('A sua viagem custou{}'.format(lng))
else:
    print('Sua viagem custou {}'.format(prc))    

