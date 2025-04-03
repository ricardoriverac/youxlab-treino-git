ano=int(input('Diga o ano que deja analisar '))
if ano % 4 == 0 and ano % 400 or ano % 100:
    print('O ano e Bissexto ')
else:
    print('O ano Não e Bissexto')
