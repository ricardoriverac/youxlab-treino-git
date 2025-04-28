def dobra(lista):
    posicao=0
    while posicao<len(valores): #Enquanto posição for menor que o tamanho da lista valores
        lista[posicao]*=2
        posicao+=1

#PROGRAMA PRINCIPAL
valores=[8,3,5,7,6,2]
print(valores)
dobra(valores)
print(f'O dobro da lista: {valores}')