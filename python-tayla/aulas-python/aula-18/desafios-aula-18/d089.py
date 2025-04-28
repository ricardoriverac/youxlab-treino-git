from time import sleep
dados = []
media = 0

while True:
    nome = input('Nome: ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))

    media = (nota1 + nota2) / 2

    dados.append([nome,[nota1, nota2], media])
    
    pergunta = input('Quer continuar? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()

    if pergunta == 'N':
        break

print('-=' * 30)
print(f'\033[1;31m{"No.":<4}{"NOME":<10}{"MÉDIA":>8}\033[m')
print('\033[1m-\033[m' * 26)

for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('\033[1m-\033[m' * 26)
    escolha = int(input('Mostrar as notas de qual aluno? (999 para interromper) '))

    if escolha <= len(dados):
        print(f'As notas de {dados[escolha][0]} são {dados[escolha][1]}')

    if escolha == 999:
        sleep(0.5)
        print('FINALIZANDO...')
        print('\033[1;36m<<< VOLTE SEMPRE >>>\033[m')
        break