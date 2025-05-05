def notas(*n, situacao=False):
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    if situacao:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados
resp = notas(6.5, 8.0, 9.2, 4.7, situacao=True)
print(resp)