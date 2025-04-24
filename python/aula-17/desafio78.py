lista = list()
for v in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os numeros digitados foram: {lista}')
print(f'O maior valor foi {max(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if max(lista) == v:
        print(f'{i}', end='ª ')
print()
print(f'O menor valor foi {min(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if min(lista) == v:
        print(f'{i}', end='ª ')