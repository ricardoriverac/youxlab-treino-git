sexo = str(input('Qual o seu Gênero? [F/M]')) .upper()
while sexo not in 'MF':
    sexo=str(input('Dados invalidos! Digite de novo por favor: '))
print('Gênero cadastrado com sucesso!')