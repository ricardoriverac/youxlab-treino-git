#UNINDO DICIONÁRIOS E LISTAS
pessoas=[]
dados={}
somaIdades=media=0
while True:
    dados['nome']=str(input('Nome: '))
    dados['sexo']=str(input('Sexo [M/F]:')).strip().upper()[0]
    while dados['sexo'] not in'MF':
        print('ERRO, você precisa digitar "M" ou "F" ')
        dados['sexo']=str(input('Sexo [M/F]:')).strip().upper()[0]
    dados['idade']=int(input('Idade: '))
    somaIdades+=dados['idade']
    escolha=str(input('Quer continua? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
         print('ERRO, você precisa digitar "S" ou "N" ')
         escolha=str(input('Quer continua? [S/N]: ')).strip().upper()[0]
    pessoas.append(dados.copy())
    dados.clear()
    if escolha=='N':
        break
print(f'A)  Ao total temos {len(pessoas)} cadastradas')
media=somaIdades/len(pessoas)
print(f'B)  A média das idades é {media:5.2f} anos')
print(f'C)  As mulheres cadastradas foram', end=' ')
for pessoa in pessoas:
    if pessoa['sexo']=='F':
        print(pessoa["nome"])
print(f'D)  Lista de pessoas a cima da média: ')
for pessoa in pessoas:
    if pessoa['idade']>=media:
        print('     ', end=' ')
        for key, value in pessoa.items():
            print(f'{key} = {value}',end=' ')
