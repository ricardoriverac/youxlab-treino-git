ano = int(input('Digite o ano em que você está: '))
bissexto = (ano % 4 == 0) or (ano % 100 == 0) or (ano % 400 == 0)
if bissexto:
    print('Esse ano é bissexto ') 
else:
    print ('Esse ano não é bissexto ')    