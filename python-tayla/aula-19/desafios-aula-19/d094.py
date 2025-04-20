dados = []
pessoas = {}
soma = quantidade = 0

while True:
    nome = input('Nome: ')
    sexo = input('Sexo: [M/F] ').upper()

    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper()

    idade = int(input('Idade: '))

    pessoas['nome'] = nome
    pessoas['sexo'] = sexo
    pessoas['idade'] = idade

    #calculando media
    soma += idade
    quantidade += 1

    dados.append(pessoas.copy())

    pergunta = input('Quer continuar? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()

    print('-=' * 20)

    if pergunta == 'N':
        break

media = soma / quantidade

print('-=' * 30)
print(f'— O grupo tem {len(dados)} pessoas')
print(f'— A média de idade é de {media} anos')
print('— As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'F':
        print(p['nome'], end=' - ')
    
print()
print('— Lista das pessoas que estão acima da média:')
for p in dados:
  if p["idade"] > media:
   for k, v in p.items():
    print(f' {k} = {v}; ', end='')
   print('\n ')

print('<< ENCERRADO >>')