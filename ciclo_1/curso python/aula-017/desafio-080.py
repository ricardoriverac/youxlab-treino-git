lista = []
for c in range(5):
    num = int(input('Digite um valor:'))
    if c == 0:
        lista.append(num)
    elif num > lista[-1]: #Pega o ultimo elemento( se o num for maior que o ultimo elemento)
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Números sorteados: {lista}')