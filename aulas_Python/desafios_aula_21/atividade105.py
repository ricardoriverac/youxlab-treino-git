def t105(*numeros, sit=False):
    """
    Analisa as médias de uma turma de alunos, retornando informações estatísticas.

    Args:
        *numeros: Um número variável de argumentos representando as médias dos alunos.

    Returns:
        str: Uma string formatada contendo o total de alunos, a maior média,
             a menor média e a média geral da turma.
             Exemplo: 'Total: 4 | Maior: 10.0| Menor: 5.5| Média: 7.875'
    """
    
    turma = {}
    soma = 0
    
    for i, media in enumerate(numeros):
        nome = f'Aluno {i+1}' 
        turma[nome] = {'media': media}
        
        
    quantidade = len(turma)
    soma = sum([aluno['media'] for aluno in turma.values()])
    media = soma / quantidade if quantidade > 0 else 0
    maxi = max(numeros)
    mini = min(numeros)
    print('='*15)
    if sit == True:
        if media > 6:
            print('Situação boa')
            
        else: 
            print('Situação ruim!')
    
    return (f'Total: {quantidade} | Maior: {maxi}| Menor: {mini}| Média: {media}')

    
resp = t105(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print(help(t105))