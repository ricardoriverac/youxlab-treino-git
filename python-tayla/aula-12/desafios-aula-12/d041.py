import datetime
ano = int(input('Digite o ano que você nasceu: '))
#variavel pro ano atual
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
idade = ano_atual - ano
if idade <= 9:
    print('Você está na categoria Mirim')
elif idade <= 14:
    print('Você eatá na categoria Infantil')
elif idade <= 19:
    print('Você está na categoria Junior')
elif idade <= 20:
    print('Você está na categoria Sênior')
else:
    print('Você está na categoria Master')