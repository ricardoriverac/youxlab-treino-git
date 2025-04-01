vel=float(input('Quantos Km você percorreu ? '))
if vel > 80:
     print('Multado!!!!Ande mais devagar')
     multa= (vel-80) * 7 
     print('Voce tem que pagar {}'.format(multa))
     print('Você ultrapassou o limite vagabundo')
else:
     print('Pode prosseguir')


