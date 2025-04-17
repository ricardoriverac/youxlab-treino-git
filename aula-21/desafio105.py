def fichaluno(*n, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas (aceita várias)
    :param situação: (opcional), indica se deve ou não mostrar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n)/dados['total']
    if situação:
        if dados['média'] > 7:
            dados['situação'] = 'BOA'
        elif 5 < dados['média'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        elif dados['média'] < 5:
            dados['situação'] = 'RUIM'
    return dados


resp = fichaluno(5.5, 2.5, 1.5, situação=True)