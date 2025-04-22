def notas(*nota, sit=False):
    resultado = {}
    resultado['total'] = len(nota)
    resultado['maior'] = max(nota)
    resultado['menor'] = min(nota)
    media = sum(nota)/len(nota) if nota else 0
    resultado['media'] = media
    if sit:
        if media >=7:
            resultado['situação'] = 'Boa'
        elif media >= 5:
            resultado['situação'] = 'Razoável'
        else:
            resultado['situação'] = 'Ruim'
    return resultado

resp = notas(7.0, 10, 6,5, sit=True)
print(resp)