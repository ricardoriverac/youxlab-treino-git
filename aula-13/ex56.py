somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehmvelho = ''
totmulher20 = 0

for pessoas in range(1, 5):
    print('----{}ª pessoa----'.format(pessoas))
    nome = input ('Nome: ')
    idade = int(input ('Idade : '))
    sexo = input ('Sexo [M/F]: ')
    somaidade += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehmvelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehmvelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomehmvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))