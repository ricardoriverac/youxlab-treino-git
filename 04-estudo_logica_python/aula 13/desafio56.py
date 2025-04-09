soma=0
mulheres=0
homem=0
media=0
for i in range(1,5):

    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [m/f]').upper()[0]
    idade = int(input('Digite a sua idade : '))

    soma = soma + idade 
    media = soma / i 

    if sexo == ['m'] and idade > maior:
        maior = idade 
        homem = nome

    if sexo == ['f'] and idade < 20:
        i_mulheres += 1

print('Media das idades é de {:.2f} '.format(media))
print('Home do mais velho é {}'.format(homem))

if mulheres ==  1:
    print('Não temos mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 anos'.format(mulheres))