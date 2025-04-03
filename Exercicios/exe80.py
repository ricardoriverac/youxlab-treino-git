#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os
#Em uma lista, ja na posição correta de inserção (sem usar o sort()).
#no final, mostre a lista ordenada na tela.

lista = []

for n in range(5):
    nn = int(input("Digite um número: "))
    
    if not lista:
        lista.append(nn)
    else:
        pos = 0
        while pos < len(lista):
            if nn < lista[pos]:
                break
            pos += 1
        lista.insert(pos, nn)
print("Lista ordenada:", lista)


