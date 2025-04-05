from datetime import date
print('Você deve se alistar?')
sexo = str(input('Qual é o seu gênero? '))
if sexo in 'Feminino feminino Mulher mulher':
    print('Você não é obrigada a se alistar no exécito.')
    deseja = str(input('Mesmo assim você deseja se alistar? '))
    if deseja in 'Sim sim':
        print('Ok, então continue preenchendo o formuláriio')
    if deseja in 'Não não':
        print('Mesmo assim continue preenchendo o formulário para caso mude de ideia')
if sexo in 'Masculino masculino Homem homem':
    print('O seu alistamento é obrigatório\nContinue preenchendo o formulário')
else:
    print('Gênero inválido. Tente novamente')
    exit()
i = int(input('Em que ano você nasceu? '))
ano = date.today().year
dma = ano - i
ada = i + 18
qtf = 18 - dma
qtjf = dma - 18
if dma < 18:
    print('Ainda não é hora de se alistar no exército, você ainda tem {} anos, seu alistamento será em {}'.format(qtf, ada))
elif dma == 18:
    print('Já está na hora de se alistar no exército')
elif dma > 18 and dma < 22:
    if qtjf == 1:
        print('Já se passou {} ano desde seu alistamento que foi em {}, se não se alistou ainda, corra!'.format(qtjf, ada))
    else:
        print('Já se passaram {} anos desde seu alistamento que foi em {}, se não se alistou ainda, corre!'.format(qtjf, ada))
elif dma > 18 and dma > 22:
    print('Já se passaram {} anos desde o seu alistamento que foi em {}, faz tempo em, se você não foi ainda o que é que você está fazendo da sua vida???'.format(qtjf, ada))