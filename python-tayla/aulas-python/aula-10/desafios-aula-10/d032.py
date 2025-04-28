import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
if ano == 0:
    ano = ano_atual
    print(f'Estamos no ano {ano}')
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')