def notas(*nota ,situacao = False):
    """
    --> Função pra analisar notas e situação de vários alunos 
    : para nota: parâmetro para receber uma ou mais notas dos alunos
    : para situação: valor opcional, falando se deve ou não mostrar a situação do aluno
    : return: retornando um valor do dicionário dados
    """
    dados = {}
    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    dados['média'] = sum(nota) / dados['total']

    if situacao == True:
        if dados['média'] >= 7:
            dados['situação'] = 'boa'
        elif 5 <= dados['média'] < 7:
            dados['situação'] = 'razoável'
        else:
            dados['situação'] = 'ruim'

    return dados

print('\033[1;35m-=\033[m' * 35)
resposta = notas(1, 2, situacao=False)
print(resposta)
