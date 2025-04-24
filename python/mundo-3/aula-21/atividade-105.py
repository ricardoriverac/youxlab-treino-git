def notas(*n, situacao=False):
    """
    Calcula estatísticas sobre um conjunto de notas de alunos.

    Parâmetros:
    - *n: uma ou mais notas (números) dos alunos.
    - situacao (bool, opcional): se True, adiciona a situação da turma com base na média.

    Retorna:
    - Um dicionário contendo:
        - quantidade: número total de notas
        - maior: a maior nota
        - menor: a menor nota
        - media: a média das notas
        - situacao: (opcional) avaliação da situação geral da turma:
            'Boa' para média >= 7
            'Razoável' para média >= 5 e < 7
            'Ruim' para média < 5
    """
    resultado = dict()
    resultado['quantidade'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['media'] = sum(n) / len(n)
    
    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'Boa'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'Razoável'
        else:
            resultado['situacao'] = 'Ruim'

    return resultado

resp = notas(5.5, 8.0, 6.5, 9.0, situacao=True)
print(resp)
