ano = int(input('insira um ano: '))
if ano % 4 == 0: 
    if ano % 100 > 0.0: 
        calculo = bool(True)
    else:
        if ano % 400 == 0: 
            calculo = bool(True)
        else:
            calculo = bool(False)
else:
    calculo = bool(False)
print(f'O ano {ano} é BISSEXTO')if calculo == True else print(f'O ano {ano} NÃO é BISSEXTO')

# depois eu descobri da existência do 'and' e do 'or' vendo a resolução do problema. dava pra ter um código menor no fim das contas.