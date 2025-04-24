lista = []
while True:
    nome = str(input('Digite o nome do aluno, por favor: ')).title()
    notaUm = float(input('Qual foi a primeira nota? '))
    notaDois = float(input('Qual foi a segunda nota? '))
    media = (notaUm + notaDois) / 2
    lista.append([nome, [notaUm, notaDois], media])
    pergunta = str(input('Gostaria de continuar? (S/N): '))
    if pergunta in 'nN':
        break
print(f'\n{"N°" :<4}{"Nome":<10}{"Média":>8}')
for i, n in enumerate(lista):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
while True:
    escolha = input('\nGostaria de ver a nota de um aluno em específico? Se não -> (digite "sair" para encerrar): ').strip().lower()
    if escolha == 'sair':
        print('\n O sistema foi encerrado!!')
        break
    if escolha.isdigit() and int(escolha) < len(lista):
        escolha = int(escolha)
        print(f'as notas de {lista[escolha][0]} são {lista[escolha][1]}')
    else:
        print('Opção inválida! Tente novamente.')