import datetime
anoNascimento = int(input('Digite o ano que você nasceu: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNascimento
if idade < 10:
    print ('Você está na categoria MIRIM. ')
elif 10 <= idade < 15:
    print ('Você está na categoria INFANTIL. ')
elif 15 <= idade < 20:
    print ('Você está na categoria JUNIOR. ')
elif idade == 20:
    print ('Você está na categoria SÊNIOR. ')
elif idade > 20:
    print ('Você está na categoria MASTER. ')
if idade > 110:
    print (f'Você tem {idade} anos. Provavelmente você já morreu :/ ')