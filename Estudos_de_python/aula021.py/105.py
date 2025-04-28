def notas(*numero, situacao=False):
    dados = {}

    dados['total'] = len(numero)
    dados['Maior'] = max(numero)
    dados['Menor'] = min(numero)
    dados['media'] = sum(numero) / len(numero)

    if situacao:
        if dados['media'] < 6:
            dados['situacao'] = 'Reprovado'
        elif dados['media'] < 7:
            dados['situacao'] = 'Recuperação'
        else:
            dados['situacao'] = 'Aprovado'

    return dados






















