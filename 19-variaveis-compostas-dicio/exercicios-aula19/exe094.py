pessoas = list()
dados = {}
pessoascadastrada = 0
somaidade = 0
mulherescadst = list()
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]')).upper().strip()
    if dados['sexo'] == 'F':
        mulherescadst.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    pessoas.append(dados.copy())
    pessoascadastrada += 1
    sair = str(input('Quer continuar [S/N] ')).upper().strip()
    if sair == 'N' :
        break
    if sair != 'N' and sair != 'S':
        print('ERRO! digite novamente...')
        while True:
            sair = str(input('Quer continuar [S/N] ')).upper().strip()
            if sair != 'N' and sair != 'S':
                print('ERRO! digite novamente...')
            if sair == 'S' or sair == 'N':
                break
media = somaidade/pessoascadastrada
print(f'-O grupo tem {pessoascadastrada} pessoas. ')
print(f'-A média do grupo é {media:.2f} anos')
print(f'-A mulheres cadastradas foram: ' , end='')
for v in mulherescadst:
    print(f'{v}', end=' ')
if pessoas[1]['idade'] > media  : 
    print('-Pessoa acima da média')
    for k , v in dados.items():
        print(f'{k} = {v}' , end=' ')