lista = []
for n in range (0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor > lista[-1]: # Se o número for o primeiro ou se o número for maior que o último elemento
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # Vai da posição 0 até a última posição
            if n <= lista[pos]: # Verifica dentro de cada posição se o número é igual ou maior que ele
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista... ')
                break
            pos+=1
print(f'Esses valores digitados em ordem foram {lista}')

                