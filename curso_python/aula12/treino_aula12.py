nome = str(input('Qual é o seu nome? '))
if nome == 'Vinícius':
    print ('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'João':
    print ('Seu nome é muito popular no Brasil.')
else:
    print ('Seu nome é muito normal...')
print (f'Tenha um bom dia, {nome}. ')