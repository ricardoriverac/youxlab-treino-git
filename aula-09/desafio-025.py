nome = str(input('Digite seu nome'))
a = nome.strip()
b = a.find('Silva')

if b != -1:
    print('Sim tem "Silva"')
else:
    print('Não tem "Silva"')    
