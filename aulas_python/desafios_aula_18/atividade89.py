ListadeAlunos = []

ComandoParada = 1
while ComandoParada != 999:
    ListadeAlunos.append(str(input('-------------------------------------\nQual o nome do aluno?: ')))
    ListadeAlunos.append(float(input('Nota 1: ')))
    ListadeAlunos.append(float(input('Nota 2: ')))
    
    Escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while Escolha != 'S' and Escolha != 'N':
        Escolha = str(input('Opção inválida\n[S/N]: ')).upper()
        
    if Escolha == 'N':
        print(ListadeAlunos[1])
    ComandoParada = int(input('999 interrompe): '))    
    