import datetime
ano = int(input('ano de nacimento: '))

data = datetime.datetime.now()
anoatual = data.year
idade = (anoatual - ano)

print(f'o atleta tem {idade} anos')

if idade > 20:
    print(f'sua classificação:Master')
elif idade <= 20:
     print(f'sua classificação:Sênior')
elif idade <= 19:
     print(f'sua classificação:junior')
elif idade <= 14:
     print(f'sua classificação:Infantil')
elif idade <= 9:
     print(f'sua classificação:Mirin')