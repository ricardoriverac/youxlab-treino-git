import datetime

for i in range(7):
    print('')

ano = int(input('Em qual ano você nasceu? '))

data_atual = datetime.datetime.now()

ano_atual = data_atual.year

idade = ano_atual - ano

