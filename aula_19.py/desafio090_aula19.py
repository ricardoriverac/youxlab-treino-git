pessoa= {}
pessoa['nome'] = str(input('Digite o Nome: ')).strip().title()
pessoa['media'] = int(input('Digite a média: '))
if pessoa['media'] >= 6:
    pessoa['situação'] = 'Aprovado'
elif 5 < pessoa['media'] < 6:
    pessoa['situação'] = 'Recuperação'
else:
    pessoa['situação'] = 'Reprovado'
print(pessoa)
for k, v in pessoa.items():
    print(f'O {k} é igual a {v}')