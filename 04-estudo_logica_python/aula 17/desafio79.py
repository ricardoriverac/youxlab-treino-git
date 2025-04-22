lista=[]
while True:
    numero=(int(input('digite um valor:')))
    if numero not in lista:
        lista.append(numero)
        print('O numero foi adicionado')
    else:
            print('ERRO o número já se encontra na lista..')
    continuar=' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar in 'N':
        break
print(f'Você digitou os valores {sorted(lista)}.')
