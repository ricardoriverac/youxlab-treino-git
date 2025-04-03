from datetime import date
anoAtual=date.today().year
anoNasc=int(input('Digite o ano que nasceu: '))
idade =anoAtual - anoNasc

if idade <= 10:
    print('Você e um atleta Mirin ')
elif idade <= 17:
    print('Você e um atleta Junior ')
elif idade <=21: 
    print('Você e um atleta jovem  ')
else:
    print('Você e um atleta sênior')


