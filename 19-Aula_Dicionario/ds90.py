ficha= {}
while True:
    nome=str(input('Nome do Aluno: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1 + nota2) / 2
    ficha[nome] = {"notas": [nota1, nota2], "media": media}
    resp= str (input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break 
print('==' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, (nome, dados) in enumerate(ficha.items()):
    print(f'{i:<4}{nome:<10}{dados["media"]:>8.1f}')
    if media > 7:
        print('Aprovado')
    elif media < 7:
        print('Reprovado')