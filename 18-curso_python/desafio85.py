lista = list()
listaPares = list()
listaImpares = list()
for valores in range(1,8):
    valor = int(input(f'Digite o {valores}° valor: '))
    if valor %2==0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)
    
lista = listaPares + listaImpares
ordem = sorted(lista)
print(f'A lista separando os números pares e ímpares é: \033[1;35{lista}\033[m')
print(f'A lista em ordem crescente é: \033[1;33{ordem}\033[m')
