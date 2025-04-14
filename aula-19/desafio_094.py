
listaPessoas = []



while True:

    nome = str(input('Nome: '))

    sexo = str(input('Sexo: ')).strip().upper()[0]



    while sexo != 'M' and sexo != 'F':

        print('Digite um sexo válido!')

        sexo = str(input('Sexo: ')).strip().upper()[0]



    idade = int(input('Idade: '))



    while idade < 0:

        print('Digite uma idade válida!')

        idade = int(input('Idade:')) 



    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]



    while resposta not in 'SN':

        print('Digite uma resposta válida!')

        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]



    print()



    pessoa = dict()

    pessoa['nome'] = nome

    pessoa['sexo'] = sexo

    pessoa['idade'] = idade



    listaPessoas.append(pessoa)



    if resposta == 'N':

        break



print(listaPessoas)



print(f'- O grupo tem {len(listaPessoas)} pessoas.')



somaIdades = 0

mediaIdade = 0

for i in range(0, len(listaPessoas)):

    somaIdades += listaPessoas[i]['idade']



    mediaIdade = somaIdades / (i + 1)

print(f'- A média de idade é de {mediaIdade:.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for i in range(0, len(listaPessoas)):
    if listaPessoas[i]['sexo'] == 'F':
        print(listaPessoas[i]['nome'], end='; ')

print()

print('- Lista de pessoas que estão acima da média: ')
for i in range(0, len(listaPessoas)):
    if listaPessoas[i]['idade'] > mediaIdade:
        print(f'nome = {listaPessoas[i]["nome"]}; sexo = {listaPessoas[i]["sexo"]}; idade = {listaPessoas[i]["idade"]};')
        print()