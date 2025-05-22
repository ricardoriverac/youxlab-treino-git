#categoria de natação
from datetime import date
dataAtual=date.today().year
print('CATEGORIA DE NATAÇÃO')
anoNasc=int(input('Em que ano você nasceu?:'))
idade= dataAtual-anoNasc
if idade<=9:
    print(f'Você tem {idade}, sua categoria é MIRIM')
elif idade>9 and idade<=14:
    print(f'Você tem {idade}, sua categoria é INFANTIL')
elif idade>14 and idade<=19:
    print(f'Você tem {idade}, sua categoria é JUNIOR')
elif idade>19 and idade<=25:
    print(f'Você tem {idade}, sua categoria é SÊNIOR')
else:
    print(f'Você tem {idade}, sua categoria é MASTER')


     
