lista = [ ]
resposta =' '
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    while True:
        resposta = input('Quer continuar? [S/N] ').upper()
        if resposta in 'SN':
            break
        print ('Algo deu errado. Digite novamente.', end=' ')
    if resposta== 'N':
        break
quantidade = len(lista)
print(f'A \033[1;31mquantidade\33[m de números digitados foi de {quantidade}')
descrescente = sorted(lista, reverse=True)
print(f'A lista em ordem \033[1;31mdecrescente\033[m é {descrescente}.')
numeroCinco = lista.count(5)
if numeroCinco == 0:
    print('Não tem número 5 na lista.')
else:
    print(f'O número 5 foi digitado, tem {numeroCinco} números 5 na lista.')

