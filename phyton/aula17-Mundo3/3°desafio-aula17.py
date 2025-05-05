#LISTA ORDENADA SEM REPETIÇÕES
lista=[]
for count in range (0,5):
    numero=int(input('Digite um número: '))
    if count==0 or numero>lista[-1]: 
        lista.append(numero)
        print('Foi adicionado na última posição')
    else:
        posicao=0
        while posicao<len(lista):
            if numero<= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Foi adicionado na posição {posicao}')
                break
            posicao+=1
print(f'os valores da são {lista}')