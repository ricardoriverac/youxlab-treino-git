#MENOR E MAIOR VALORES EM LISTA
numeros=[]
for contador in range(0,5):
    numeros.append(int(input('Digite um número: ')))
print(numeros)
for posicao, numero in enumerate(numeros):
    if numero==max(numeros):
        print(f'O maior valor é o {numero} na posição {posicao}')
    if numero==min(numeros):
        print(f'O menor valor é o {numero} na posição {posicao}')
    