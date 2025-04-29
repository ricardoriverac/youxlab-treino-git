soma = 0
maisVelho = 0
nomeVelho = ''
mulheres=0

for c in range(1, 4):
    print(f'---- {c} Pessoa ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').strip().upper()
    
    soma += idade
    
    if sexo == 'M':
        if idade > maisVelho: 
            maisVelho = idade
            nomeVelho = nome

    elif sexo =='F' and idade < 20:
            mulheres += 1

media = soma/3

print('O homem mais velho tem {} anos e seu nome é {}.'.format(maisVelho,nomeVelho))
print('A média de idade do grupo é {}. '.format(media))
print('Ao todo são {} mulheres '.format(mulheres))
    
