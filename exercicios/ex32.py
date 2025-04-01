from datetime import date
ano = int (input ('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ("o ano {} é BISSEXTO !! ".format(ano))
else:
      print ("o ano {} NÃO é BISSEXTO !! ".format(ano))