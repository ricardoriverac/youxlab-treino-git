oma = 0
cont_mulheres = 0
media = 0
maior = 0
nomeHomemMais_Velho = ''


for cont in range(1,5):

    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [M/F]').upper()[0]
    idade = int(input('Digite a sua idade : '))
    print('-'*20)

    soma = soma + idade #faz a soma entre todas as idades
    media = soma / cont #pegaa soma das idades e divide pelo numero de pessoas

    if sexo == 'M' and idade > maior:
        maior = idade
        nomeHomemMais_Velho = nome

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

print('Media das idades é de {:.2f} '.format(media))
print('Nome do mais velho é {}'.format(nomeHomemMais_Velho))

if cont_mulheres == 0:
    print('Não temos mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 ano'.format(cont_mulheres))a