def notas(*nota,sit=False):
    """
    param nota: recebe o valor das notas
    param sit: receber um valor (opcional) da situação do aluno
    param return: retorna o valor do dicionario criado
    """
    aluno = {}
    aluno['total'] = len(nota)
    aluno['maior'] = max(nota)
    aluno['menor'] = min(nota)
    if sit:
        soma = sum(nota)
        aluno['media'] = soma/aluno['total']
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


#programa principal
resp = notas(5, 1, 2.2 , 4 , 3.5 , 5, 10 , sit=True)
print(resp)
