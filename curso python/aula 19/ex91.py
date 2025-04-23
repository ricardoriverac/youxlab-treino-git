import random
resultados = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6)
}
print ('-=' * 4, f'\033[35mRESULTADO DOS DADOS\033[m','-=' * 4 )
for jogador, valor in resultados.items():
    print (f'{jogador} tirou o valor = {valor}')
listaResultados = list(resultados.items())
for elementoAtual in range (len(listaResultados)):
    for elementosSeguintes in range (elementoAtual + 1, len(listaResultados)):
        if listaResultados[elementosSeguintes][1] > listaResultados[elementoAtual][1]:
            listaResultados[elementoAtual], listaResultados[elementosSeguintes] = listaResultados[elementosSeguintes], listaResultados[elementoAtual]
print ('-=' * 4, f'\033[35mRANKING FINAL\033[m','-=' * 4 )
indice = 1
for jogador , valor in listaResultados:
    print (f'{indice}º lugar: {jogador} com o resultado = {valor}')
    indice += 1