import time

nota1 = nota2 = media = 0
dados = []

while True:
    nomes = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nomes, [nota1, nota2], media])  
    resp = input('\nQuer continuar? [S/N] ').strip().lower()[0]
    if resp == 'n':
        break

print('\033[m', 30*'-')
print('\033[1;37mNº----- Nome ------------ Média \033[m')
print(20*'-')
for pos, valor in enumerate(dados):
    print(f'{pos:<5} {valor[0]:<15} {valor[2]:>6.1f}')
print(20*'-')

while True:
    resp = int(input('Deseja mostrar notas de qual aluno: \033[1;33m(999 Interrompe)\033[m '))
    if resp == 999:
        print('\033[m')
        break
    if resp >= len(dados) or resp < 0:
        print(f'\033[1;31mOps... Tente novamente. Não há essa opção\033[m')
    else:
        print(f'As notas de \033[1;36m{dados[resp][0]}\033[m são: {dados[resp][1]}')
print('FINALIZANDO...')
time.sleep(1)
print('='*10, 'VOLTE SEMPRE', '='*10)