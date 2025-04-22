from time import sleep
lista = []
media = soma = 0
while True:
    nome = input('Nome: ')
    notaUm = float(input('Nota 1: '))
    notaDois = float(input('Nota 2: '))
    media = notaUm+notaDois/2
    lista.append([nome, [notaUm, notaDois], media])        
    
    maisAlunos = input('Você deseja continuar? \033[33m[S/N]:\033[m ').upper()
    while maisAlunos != 'S' and maisAlunos != 'N':
            print('\033[31mErro na digitação!\033[m Tente novamente! ')
            maisAlunos = input('Você deseja continuar? \033[33m[S/N]:\033[m ').upper()
    
    if maisAlunos == 'N':
        break

print('-='*20)
print(f'{"No.":<4} {"NOME ":<10} {"MÉDIA ":>8}')
print('-'*30)
for n, m in enumerate(lista):
    print(f'{n:<4}{m[0]:<10}{m[2]:>8.1f}')
print('-='*20)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == '999':
        print('FINALIZANDO...')
        sleep(3)
        break
    else:
        print(f'Notas de {lista[notas][0]} são {lista[notas][1]} ')
        
        

    