sexo = ''
while sexo not in ['f', 'm']:
    sexo = str(input('Digite o sexo [M/F]: ')).lower()
if sexo == 'm' or 'f':
    print('valor correto')
