pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'A média de {pessoa["nome"]}: '))

if pessoa['media'] >= 6:
    pessoa['situacao'] = '\033[1;32mAprovado\033[m'
else:
    pessoa['situacao'] = '\033[1;31mReprovado\033[m'

print('-' * 40)
print('\033[1;37mINFORMAÇOẼS\033[m'.center(40))
print('-' * 40)

print(f'O nome é {pessoa["nome"]}. ')
print(f'A média {pessoa["media"]}')
print(f'Contudo, sua situação é: {pessoa["situacao"]}')