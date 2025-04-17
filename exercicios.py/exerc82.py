lista = [ ]
listaPares = [ ]
listaImpares = [ ]
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    if numeros %2==0:
        listaPares.append(numeros)
    else:
        listaImpares.append(numeros)
    while True:
        resposta = input('Quer continuar? [S/N] ').upper()
        if resposta in 'SN':
            break
        print('Algo deu errado. Digite de novo', end = '')
    if resposta == 'N':
        break
print(f'Lista com todos os números: \033[1;35m{lista}\033[m')
print(f'Lista com os números pares: \033[1;36m{listaPares}\033[m')
print(f'Lista com os números ímpares: \033[1;33m{listaImpares}\033[m')