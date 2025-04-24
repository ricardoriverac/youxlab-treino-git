print('Descubra se o ano é bissexto.')
ano = int(input('Digite o Ano: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é um ano bissexto')