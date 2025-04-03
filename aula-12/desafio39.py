nome = input('Nome: ')
ano = int(input('Ano de nascimento: '))
r = 2019-ano
if r > 18:
    print('{} você deveria estar alistado!'.format(nome))
elif r < 18:
    print('{} você é muito novo, não poderá se alistar agora'.format(nome))
else:
    print('{} esse ano você precisa se alistar'.format(nome))
