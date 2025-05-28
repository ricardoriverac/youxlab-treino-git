from datetime import date
atual = date.today().year
ns = int(input('que ano você nasceu?: '))
idade = atual  -  ns
print('quem nasceu em {} tem {} anos em {}' .format(ns, idade, atual))
if idade == 18:
    print('se aliste o quanto antes. ')
elif idade < 18:
    saldo = 18 - idade
    print(' ainda falta {} anos para o alistameto ' .format(saldo))
elif  idade > 18:
    saldo = idade - 18
    print(' ja passou {} anos para vc se alistar. ' .format(saldo))
