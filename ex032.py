ano= int(input('Digite um ano: '))
if ano % 4 == ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('o ano não é bissexto!')
