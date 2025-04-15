
pessoas = {}

pessoas['nome'] = str(input('Nome: '))

pessoas['media'] = float(input(f'Média de {pessoas["nome"]}: '))

if pessoas["media"] >= 6:
    pessoas['sit'] = 'aprovado'
else:
    pessoas['sit'] = 'reprovado' 
print('--'*30)
print(f'''Nome é igual a {pessoas["nome"]}
Média é igual a {pessoas["media"]}
A situação é de {pessoas["sit"]}''')