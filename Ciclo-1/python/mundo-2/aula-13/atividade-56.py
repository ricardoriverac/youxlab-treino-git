somaidade = 0
velho = 0
hnome = ''
idade20 = 0

for i in range(1, 5):
    print(f'\nPessoa {i}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().upper()

    somaidade += idade

    if sexo == 'M':
        if idade > velho:
            velho = idade
            hnome = nome
    elif sexo == 'F':
        if idade < 20:
            idade20 += 1

media = somaidade / 4

print(f'\nA média de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho tem {velho} anos e se chama {hnome}')
print(f'Existem {idade20} mulher(es) com menos de 20 anos.')
