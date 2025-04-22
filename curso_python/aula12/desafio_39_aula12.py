import datetime
ano = int(input('Em que ano você nasceu? '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - ano
if idade < 18:
    print (f'Você deverá se alistar em {18-idade} anos')
elif idade == 18:
    print ('Já está na hora de se alistar')
else:
    print (f'Você deveria ter se alistado há {idade-18} anos')