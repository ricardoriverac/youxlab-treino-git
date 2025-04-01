#estrutura condicional aninhada
nome = str(input('Qual é o seu nome? '))
if nome == 'Tayla':
    print('Que nome daora!')
elif nome == 'Pedro' or nome == 'Maria' or  nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia {nome}')