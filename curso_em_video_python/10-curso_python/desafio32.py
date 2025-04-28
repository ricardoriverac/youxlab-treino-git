ano = int(input('Digite um ano: '))
anoBissexto = ano % 4
print(anoBissexto)
if anoBissexto ==0 :
    print('O ano {} é bissexto. '.format(ano))
else :
    print('O ano {} não é bissexto. '.format(ano))
    