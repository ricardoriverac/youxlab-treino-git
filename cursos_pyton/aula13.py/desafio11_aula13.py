soma = 0
cmulheres = 0
media = 0
maior = 0
homemvelho = ''
for cont in range(1,5):
    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [M/F]').upper()[0]
    idade = int(input('Digite a sua idade : '))
    print('-'*20)
    soma = soma + idade
    media = soma / cont 
    if sexo == 'M' and idade > maior:
        maior = idade
        homemvelho = nome
    if sexo == 'F' and idade < 20:
        cmulheres += 1
print('Media das idades é de {:.2f} '.format(media))
print('O nome do homem mais velho é {}'.format(homemvelho))
if cmulheres == 0:
    print('Não temos mulheres no grupo !')
else:
    print('Ao todo temos {} mulheres menores de 20 anos'.format(cmulheres))