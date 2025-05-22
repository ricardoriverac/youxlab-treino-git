from datetime import date
print('Saiba qual é a categoria do atleta:')
a = int(input('Digite o ano de nascimento do atleta: '))
d = date.today().year
idade = d-a 
print('O(a) atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Ele(a) é classificado(a) como: mirim!')
elif idade <= 14:
    print('Ele(a) é classificado(a) como: infantil!')
elif idade <= 19:
    print('Ele(a) é classificado(a) como: junior!')
elif idade <= 25:
    print('Ele(a) é classificado(a) como: sênior!')
elif idade > 25:
    print('Ele(a) é classificado(a) como: master!')