from datetime import date
ano=int(input('Me fale um ano qualquer. Coloque 0 para o ano atual. '))
if ano == 0:
    ano = date.today().year
if  ano % 4 == 0 and ano % 100 !=0 or  ano % 400 == 0: 
    print('O ano {} é bissexto! '.format(ano))
else: print ('O ano {} nao é bissexto! '.format(ano))