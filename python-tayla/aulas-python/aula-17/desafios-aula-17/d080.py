valores = []

for c in range(0,5):
    numero = int(input('Digite um valor: '))
    posicao = 0

    if c == 0 or numero > valores[-1]:
        print('Adicionado ao final da lista...')
        valores.append(numero)
    else:
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram \033[1m{valores}\033[m')