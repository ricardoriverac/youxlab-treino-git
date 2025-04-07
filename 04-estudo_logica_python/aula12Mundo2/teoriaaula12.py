nome=str(input('Qual é seu nome?'))
if nome ==' Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome =='Maria' or nome =='Paulo':
     print('Seu nome é popular no Brasil')
elif nome in 'Ana Claudia Jessica Julia ':
    print('Belo nome feminino!')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}!'. format(nome))