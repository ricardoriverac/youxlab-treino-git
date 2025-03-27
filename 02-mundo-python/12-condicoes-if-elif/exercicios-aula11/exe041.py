from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade =  atual - nascimento
print(f'Quem nasceu em {nascimento} tem hoje em día {idade} anos ')
print('Este atleta terá sua classe  ', end="")
if idade < 9 :
    print('MIRIM')
elif idade <= 14 :
    print('INFANTIL')
elif idade <= 19 :
    print('JUNIOR')
elif idade <= 25 :
    print('SENIOR')
elif idade >= 25 :
    print('MASTER')        