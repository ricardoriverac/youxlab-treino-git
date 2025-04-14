import time
dados = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])  
    resp = input('\nQuer continuar? [S/N] ').strip().lower()[0]
    if resp == 'n':
        break

print(30*'-')
print('\033[1;37mNº     Nome              Média \033[m')
print(30*'-')

for pos, aluno in enumerate(dados):
    print(f'{pos:<6}{aluno[0]:<18}{aluno[2]:>5.1f}')
print(30*'-')

while True:
    resp = int(input('Deseja mostrar notas de qual aluno? \033[1;33m(999 interrompe): '))
    if resp == 999:
        print('\033[m')
        break
    if resp >= len(dados):
        print(f'\033[1;31mOps... Tente novamente. Não há essa opção.\033[m')
    else:
        print(f'\033[1;36mAs notas de {dados[resp][0]} são: {dados[resp][1]}\033[m')

print('FINALIZANDO...')
time.sleep(1)
print(10*'=', 'VOLTE SEMPRE', 10*'=')


