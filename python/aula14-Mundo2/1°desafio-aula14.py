#VALIDAÇÃO DE DADOS
sexo=str(input('Seu sexo é [M/F]?:')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('ERRO\nDado inválido, qual o seu sexo [M/F]?:')).strip().upper()[0]
print(f'Seu sexo é {sexo}')