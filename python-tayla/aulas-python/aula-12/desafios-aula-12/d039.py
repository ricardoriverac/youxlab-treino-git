import datetime
ano = int(input('Em qual ano você nasceu? '))
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
idade = ano_atual - ano
if idade < 18:
    print(f'Faltam {18 - idade} anos pra você se alistar')
elif idade > 18:
    print(f'Você deveria ter se alistado {idade - 18} anos atrás')
else:
    print('Você deve se alistar esse ano')