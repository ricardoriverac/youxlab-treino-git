import datetime
ano = int(input('ano de nacimento: '))

data = datetime.datetime.now()
anoatual = data.year
idade = (anoatual - ano)

print(f'nacidos em {ano} tem {idade} anos')

if idade < 18:
    falta = (18-idade)
    alist = (ano + 18)
    print(f'''faltam {falta} ano(os) para o seu alistamento
    seu alistamento vai ser em {alist}''')
elif idade == 18:
    print('Você deve se alistar ainda esse ano')
elif idade > 18:
    falta2 = (idade - 18)
    print(f'você deveria ter se alistado fazem {falta2} ano(os)')