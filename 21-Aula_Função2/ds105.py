def notas():
    """
    Função que registra o nome dos alunos e suas duas notas, calcula a média individual,
    e ao final apresenta:
        - Listagem de alunos com médias
        - Maior nota da turma
        - Menor nota da turma
        - Média geral da turma
        - Quantidade total de notas lançadas
    """
    ficha = {}
    todas_as_notas = []

    while True:
        nome = str(input('Nome do Aluno: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        ficha[nome] = {"notas": [nota1, nota2], "media": media}
        todas_as_notas.extend([nota1, nota2])

        resp = str(input('Quer continuar ? [S/N] '))
        if resp.lower() == 'n':
            break

    print('==' * 30)
    print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
    print('-' * 30)
    for i, (nome, dados) in enumerate(ficha.items()):
        print(f'{i:<4}{nome:<10}{dados["media"]:>8.1f}')

    # Estatísticas da turma
    maior_nota = max(todas_as_notas)
    menor_nota = min(todas_as_notas)
    media_turma = sum(todas_as_notas) / len(todas_as_notas)
    total_notas = len(todas_as_notas)

    print('\nResumo da Turma:')
    print(f'Maior nota da turma: {maior_nota:.1f}')
    print(f'Menor nota da turma: {menor_nota:.1f}')
    print(f'Média geral da turma: {media_turma:.1f}')
    print(f'Total de notas lançadas: {total_notas}')

notas()
