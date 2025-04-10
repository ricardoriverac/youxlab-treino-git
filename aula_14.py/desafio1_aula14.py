masculino = 'M'
feminino = 'F'
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ').upper())
    if sexo != 'M' and sexo != 'F':
        print('ERRO, digite novamente')
feminino = 'F'
masculino = 'M'
if sexo == 'M':
    print('A pessoa é do sexo masculino.')
else:
    print('A pessoa é do sexo feminino.')