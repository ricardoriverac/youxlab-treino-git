anoNasc=int(input('Diga o ano que nasceu: '))
anoAtual=int(input('Diga o ano atual: '))
idade=anoAtual - anoNasc

if idade == 18:
    print('Você ja esta na idade de alistamento ')
elif idade >18:
    print('Você ja passou da idade de se alistar ')
else:
    print('Você não possui idade para o alistamento ')