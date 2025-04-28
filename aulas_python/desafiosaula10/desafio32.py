ano = int(input('Digite um ano qualquer: '))
anoBissexto = ano % 4 
anoBissextoDivisivelPor100 = ano % 100
anoBissextoDivisivelPor400 = ano % 400
#O ano bissexto tem que ser divisivel por 4 e 400 e não pode ser divisivel por 100
if anoBissexto == 0 and anoBissextoDivisivelPor100 != 0 or anoBissextoDivisivelPor400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO! '.format(ano))
