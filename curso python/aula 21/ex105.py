def notas(*Notas, Situacao=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :Return:
    Dicionário com várias informações sobre a situação da turma.
    """
    Resultado = {}
    Resultado['Total'] = len(Notas)
    Resultado['Maior'] = max(Notas)
    Resultado['Menor'] = min(Notas)
    Resultado['Media'] = sum(Notas) / len(Notas)
    if Situacao:
        if Resultado['Media'] >= 7:
            Resultado['Situacao'] = 'Boa'
        elif Resultado['Media'] >= 5:
            Resultado['Situacao'] = 'Razoável'
        else:
            Resultado['Situacao'] = 'Ruim'
    return Resultado
Resposta = notas(5.5, 2.5, 1.5, Situacao=True)
print(Resposta)
help(notas)
