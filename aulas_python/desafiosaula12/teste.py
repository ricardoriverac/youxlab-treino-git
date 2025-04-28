nome = input('Qual o seu nome?: ')
if nome == 'Iza':
    print('Que nome bonito! ')
elif nome == 'Ana' or nome == 'Keverson' or nome == 'Luiz':
    print('Seu nome é bem popular no Brasil ')
else:
    print ('Seu nome é bem comum')
print('Tenha um bom dia {}!!!'.format(nome))
