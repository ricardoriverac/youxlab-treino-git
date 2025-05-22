velho = 0
cont = 0
media = 0
for c in range(1, 5):
    print('----{}ª PESSOA----'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: '))
    media += idade
    if sexo.strip().upper() == 'M':
        if idade > velho:
            velho = idade
            nvel = nome
    if sexo.strip().upper() == 'F':
        if idade < 21:
            cont += 1
mediaf = media / 4
print('A média de idade do grupo é {}.\nO homem mais velho é {}, de {} anos.\nHá {} mulheres com menos de 20 anos.'.format(mediaf, nvel, velho, cont))