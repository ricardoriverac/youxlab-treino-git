lista = list()

while True:
    nome = str(input('\033[34mQual o nome do aluno?: \033[m'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha not in ['S', 'N']:
        escolha = str(input(f'\033[31mNão temos a opção "{escolha}"\n\033[33m[S/N]: \033[m')).upper()

    if escolha == 'N':
        break

print('\033[36m-=\033[m'*30)
print(f'\033[1;37m{"No.":<4}{"NOME":<10}{"MÉDIA":>8}\033[m')
print('\033[36m-\033[m'*30)

for i, a in enumerate(lista):
    print(f'\033[32m{i:<4}{a[0]:<10}{a[2]:>8.1f}\033[m')

while True:
    print('\033[36m-\033[m'*30)
    opc = int(input('Mostrar nota de qual aluno? (999 para o programa): '))
    if opc == 999:
        print('\033[31mEncerrando...\033[m')
        break    
    if 0 <= opc < len(lista):
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')

print('\033[1;32m=-=-=-= VOLTE SEMPRE =-=-=-=\033[m')