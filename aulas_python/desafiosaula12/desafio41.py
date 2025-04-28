ano = float(input('Que ano você nasceu?: '))
if ano>=2016:
    print('Sua categoria na Confederação Nacional de Natação é {}MIRIM!{} '.format('\033[36m', '\033[m'))
elif ano>=2011:
    print('Sua categoria na Confederação Nacional de Natação é {}INFANTIL!{} '.format('\033[36m', '\033[m'))
elif ano>=2006:
    print('Sua categoria na Confederação Nacional de Natação é {}JUNIOR!{} '.format('\033[36m', '\033[m'))
elif ano>=2005:
    print('Sua categoria na Confederação Nacional de Natação é {}SÊNIOR!{} '.format('\033[36m', '\033[m'))
elif ano<2005:
    print('Sua categoria na Confederação Nacional de Natação é {}MASTER!{} '.format('\033[36m', '\033[m'))  
      