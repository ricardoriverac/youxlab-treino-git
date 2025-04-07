total_idade = 0
idade_maior_masculino = 0
nome_masculino = ''
feminino = 0
for c in range(0, 4):
    print('\033[97m-=' * 3, '\033[92m{}ª\033[97m Pessoa'.format(c + 1), '-=' * 3)
    nome = input('Nome: ').capitalize().title()
    idade = int(input('Idade: '))
    total_idade += idade
    sexo = input('Sexo [M/F]: ').lower()
    if sexo == 'm' and idade > idade_maior_masculino:
        idade_maior_masculino = idade
        nome_masculino = nome
    elif sexo == 'f' and idade < 20:
        feminino += 1
media_idade = total_idade / 4

print('''\033[97mA média de idade do grupo é de \033[32m{}\033[97m anos.

O homem mais velho tem \033[32m{}\033[97m anos e se chama \033[32m{}\033[97m

Ao todo são \033[32m{}\033[97m mulheres com menos de \033[32m20\033[97m anos'''.format(media_idade, idade_maior_masculino, nome_masculino, feminino))