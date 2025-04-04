lista = []
maior = menor = 0
for cont in range(0,5):
    numero = int(input(f'Digite o valor : '))
    if cont == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Foi adicionado a ultima posição...')
    else:
        pos = 0
        while pos < len(lista) :
            if numero <= lista[pos] :
                lista.insert(pos,numero)
                print(f'Adicionado a posição {pos}')
                break
        pos += 1
print(f'Os valores digitados {lista}')
