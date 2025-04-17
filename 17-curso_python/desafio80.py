lista = [ ]
for numeros in range (1, 6):
    posicao = 0
    numero = int(input(f'Digite o {numeros}° número: '))

    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adcionado ao final da lista.')
    else :
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado a posição {posicao} da lista')
                break
            posicao += 1

print (lista)
    