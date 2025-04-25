print('1°TESTE')
valores=[]
valores.append(2)
valores.append(5)
valores.append(9)
valores.append(4)
for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} achei o número {valor}')
print('Final da Lista')

print('2°TESTE')
valores=[]
for contador in range (0,5):
    valores.append(int(input('Digite um número: ')))  #adiciona os valores digitados em uma lista
for posicao, valor in enumerate(valores): #para cada posição e valor em valores
    print(f'Na posição {posicao} achei o número {valor}')
print('Final da Lista')

print('3°TESTE')
listaA=[1,2,3,4]
listaB=listaA  #LIGOU AS DUAS LISTAS
listaB[2]=8  #modificou as DUAS pois elas estão LIGADAS
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')

print('4°TESTE')
listaA=[1,2,3,4]  #[:]--> recebe todos os valores de listaA
listaB=listaA[:]  #COPIOU A LISTA não estão ligadas
listaB[2]=8       #NÃO modificou as duas pois NÃO estão ligadas
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')


