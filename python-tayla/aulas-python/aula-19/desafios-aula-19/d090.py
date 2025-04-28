dados = {'nome': '', 'media': '', 'situacao': ''}

nome = input('Nome: ')
media = int(input(f'Média de {nome}: '))
dados['nome'] = nome
dados['media'] = media

if media >= 7:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'

print('-=' * 15)
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situação é igual a {dados["situacao"]}')