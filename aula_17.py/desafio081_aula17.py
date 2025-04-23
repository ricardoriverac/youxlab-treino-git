lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar? [S / N]: ')).upper()[0]
    if cont in 'N':
        break
print(f'Foram digitados {len(lista)} valores. ')
print(f'Os valores em ordem decresente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'Sim o valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')