import datetime

ano = int(input('ano de nacimento: '))
data = datetime.datetime.now()
anoatual = data.year
idade = (anoatual - ano)
print(f'O atleta tem {idade} ano(os)')

if idade <= 9.0:
    print('Classificação: Mirim')

elif 9.0 < idade < 14.0:
    print('Classificação: Infantil')

elif 14.0 <= idade < 19.0:
    print('Classificação: Júnior')

elif 19.0 <= idade < 25.0:
    print('Classificação: Sênior')

else:
    print('Classificação: Master')