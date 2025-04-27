#BOLETIM COM LISTA COMPOSTA
lista=[]
alunos=[]
while True:
    nome=str(input('Nome: '))
    nota1=float(input('1°Nota: '))
    nota2=float(input('2°Nota: '))
    escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    alunos.append(lista[:])
    lista.clear()
    if escolha=='N':
        break
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
for indice, aluno in enumerate(alunos):
    media=(aluno[1]+aluno[2])/2
    print(f'{indice:<4}, {aluno[0]:<9}, {media}')
while True:
    mostrar=int(input('Mostrar nota do aluno? (999 para parar): '))
    if mostrar==999:
        break
    if mostrar<len(alunos):
        print(f'As notas do(a) {alunos[mostrar][0]} são {alunos[mostrar][1]} e {alunos[mostrar][2]}')
    else:
        print('Aluno não cadastrado!')