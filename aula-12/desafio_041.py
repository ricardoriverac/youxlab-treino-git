from datetime import date

atual = date.today().year

nasc = int(

    input('Digite o ano de nascimento: ')
)

idade = atual - nasc

print(
    'O atleta tem {} anos de idade.'
    .format(idade)
)

if idade <= 9.0:
    print(
        'Classificação: Mirim'
    )

elif 9.0 < idade < 14.0:
    print(
        'Classificação: Infantil'
    )

elif 14.0 <= idade < 19.0:
    print(
        'Classificação: Júnior'
    )

elif 19.0 <= idade < 25.0:
    print(
        'Classificação: Sênior'
    )

else:
    print(
        'Classificação: Master'
    )