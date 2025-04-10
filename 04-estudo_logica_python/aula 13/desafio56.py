soma=0
mulheres=0
homemvelho=0
media=0
nomehomem=''
for i in range(1,5):

    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [m/f]').upper()
    idade = int(input('Digite a sua idade : '))
    print('-'*40)
    soma += idade 
    media = soma / 4
    if i == 1 and sexo in 'Mm':
       homemvelho =idade
       nomehomem= nome

    if sexo in 'Mm' and idade > homemvelho:
        homemvelho= idade 
        nomehomem=nome

    if sexo in 'Ff' and idade < 20:
        mulheres += 1

print('Media das idades é de {:.2f} '.format(media))
print('Home do mais velho é {}'.format(nomehomem))

if mulheres ==  1:
    print('Não temos mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 anos'.format(mulheres))