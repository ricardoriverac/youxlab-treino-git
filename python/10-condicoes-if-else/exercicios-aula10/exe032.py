from datetime import date
ano = int(input('Digite um ano qualquer !"0" pra mostrar seu ano atual: '))
if ano == 0 :
    atual = date.today().year
    if atual % 4 == 0 or atual % 100 == 0 or atual % 400 == 0 :
        print(f'Esse ano {atual} é bissexto')
    else:
        print(f'Esse ano {atual} não é bissexto')    
elif ano % 4 == 0 or ano % 100 == 0 or ano % 400 == 0 : 
    print(f'Esse ano {ano} é bissexto')
else:
    print(f'Esse ano {ano} não é bissexto')     