lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    maisValor = input('Deseja continuar? \033[33m[S/N]\033[m:').upper()
    if maisValor == 'N':
        break
print(f'Você digitou \033[34m{len(lista)} ELEMENTOS\033[m ')
lista.sort(reverse=True)
print(f'Os valores da \033[36mORDEM DECRESCENTE\033[m são {lista}')
if 5 in lista:
    print(f'O \033[35mVALOR 5\033[m faz parte da lista e está na posição {lista.index(5)}! ')
else:
    print('O \033[35mVALOR 5\033[m NÃO faz parte da lista! ')
