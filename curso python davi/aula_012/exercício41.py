from datetime import date
at = date.today().year
ns = int(input('ano de nascimento: '))
idade = at - ns
print(' o atleta tem {} anos. '.format (idade))
if idade <= 9:
    print('classificação mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior. ')
elif idade <= 25:
    print('senior')
elif idade <= 130:
    print('master')
else:
    print('ta morto já')
