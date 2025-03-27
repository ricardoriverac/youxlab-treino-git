from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual =  date.today().year
idd = atual - nasc
alist = 18
falta = alist - idd
deve = nasc + alist
if idd < alist :
    print(f'Quem nasceu em {nasc} tem {idd} anos em {atual}')
    print(f'Ainda falta {falta} anos para o alistamento')
    print(f'Seu alistamento é em {deve}')
elif idd == alist :
    print('Você deve se alistar IMEDIATAMENTE')
elif idd > alist :
    print(f'Quem nasceu em {nasc} tem {idd} anos em {atual}')
    devria = idd - alist
    print(f'Seu alistamento deveria ser a {devria} anos atrás')
    f = atual - devria
    print(f'Seu alistamento foi {f}')
