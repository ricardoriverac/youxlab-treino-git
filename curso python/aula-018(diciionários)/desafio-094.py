pessoas = {}
lista = []
idadeNome = []
iadadePessoas = []
mulheresLista = []
pessoasAcimaM = []
cont = 0
while True:
    nome = pessoas['nome'] = str(input("Digite o nome: "))
    idadeNome.append(nome)
    cont += 1
    idade = pessoas['idade'] = int(input('Digite a idade: '))
    idadeNome.append(idade)
    iadadePessoas.append(idade)
    sexo = pessoas['sexo'] = str(input('Qual o sexo? F/M: ')).upper()
    if sexo == 'F':
        mulheresLista.append(nome)
    # lista.append(pessoas.copy())
        # mulheresLista.append(pessoas.items())
        # mulheresLista.copy()
    continuar = str(input('Quer continuar? S/N')).upper()
        
    somaIdade = sum(iadadePessoas)
    mediaIdade = somaIdade / cont
    for c in pessoas:
        if pessoas['idade'] > mediaIdade:
            pessoasAcimaM.append(pessoas['nome'])
    if continuar == 'N':
        break
    # if 'F' in pessoas['sexo']:
    #     mulheresLista.append(pessoas.items())

somaIdade = sum(iadadePessoas)
mediaIdade = somaIdade / cont
# if nome in mulheresLista:
#     print('-=' * 30)
#     print(f'- As mulheres do grupo são {mulheresLista}')
#     print('-=' * 30)
# elif nome not in mulheresLista:
#     print('Não há mulheres no grupo')
print(f'As mulheres do grupo são: {mulheresLista}')
print(f'- As pessoas com idade acima da média são {pessoasAcimaM}')
print(f'- A média de idade do grupo é {mediaIdade:.2f}')
print(f'- {cont} pessoas foram cadastradas!')
for pessoa in lista:
    print(pessoa)


        
