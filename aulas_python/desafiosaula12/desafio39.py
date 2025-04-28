idade = int(input('Que ano você nasceu?: '))
ano = idade - 2007
if idade == 2007:
    print('Você tem que se alistar ao serviço militar ')
elif idade>2007:
    print('Você ainda vai ter que se alistar ao serviço militar daqui a {} ano '.format(ano))
elif idade<2007:
    print('Já passou do tempo do alistamento tem {} anos '.format(ano))
