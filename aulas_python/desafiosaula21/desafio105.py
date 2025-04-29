def notas(* n, sit = False):
    """
    -> Funçao para analisar notas e situações de vários alunos.
    :param n: Uma ou várias notas dos alunos.
    :param sit: (opcional) opção para ver a situção dos alunos
    :return: Dicionário com informações da turma.
    """
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/len(n)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >=5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic
        
resposta = notas(4.5, 8.5, 9.0, 10.0, 5.3, sit=True)
print(resposta)
# help(notas)


