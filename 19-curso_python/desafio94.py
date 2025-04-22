pessoas = dict()
mulheres = []
quantMulheres = 0
idadeAcimaMedia = ''
idade = [ ]
listaPessoas = []
pessoa = 0

while True:
    enfeite = ('=' * 40)
    print(f'{enfeite} PESSOA {enfeite}')

    nome = str(input('Nome: '))
    anos = int(input('Idade: '))
   
    
    pessoas['nome'] = nome
    pessoas['idade'] = anos
    
    listaPessoas.append(pessoas.copy())
    idades = sum(idade)
    idade.append(anos)

    while True:
        genero = str(input('Genêro: [M/F] ')).upper()[0]
        print(enfeite)
        if genero in 'MF':
            break
        print('Algo deu errado, digite novamente.',end='')
    if genero == 'F':
        quantMulheres += 1
        pessoas['genero'] = genero
        mulheres = pessoas['nome'] 
    


    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('Algo deu errado. Digite novamente.', end='')
    if resposta == 'N':
        break

media = idades/len(pessoas)
print(listaPessoas)
if anos > media:
    idadeAcimaMedia = pessoas['nome']


print(f'A quantidade de pessoas cadastradas foi de {len(pessoas)} pessoas. ')
print(f'A média da idades das pessoas é de {media:.0f}')
print(f'As mulheres cadastradas foi {mulheres} .')
print(f'As pessoas com idade maior que a média é {idadeAcimaMedia}')