from datetime import datetime
ano = int(input('Em que ano você nasceu? '))
anoatual = datetime.now().year
idade = anoatual - ano
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')