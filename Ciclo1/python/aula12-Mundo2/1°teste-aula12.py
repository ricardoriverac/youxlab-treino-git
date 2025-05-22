#Estrutura cindicional aninhada
nome=str(input('Digite seu nome:'))
if nome=="Sophia":
    print('Que nome bonito!')
elif nome=="Sarah" or nome=="Andressa":
    print('O seu nome é legal.')
elif nome in "Ana Alice Julia":
    print('Seu nome é um belo nome feminino!')
else:
    print('Que nome feio!')
print(f'Bom dia, {nome}!!')