aluno = {}
aluno['nome'] = input ('Digite o nome do aluno: ')
primeiraNota = float (input('Digite a primeira nota: '))
segundaNota = float (input('Digite a segunda nota: '))
media = (primeiraNota + segundaNota) / 2
aluno['media'] = media
if media <= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print ('-=' * 4, f'informações do aluno','-=' * 4 )
for chave, valor in aluno.items():
    print (f'{chave}: {valor}')