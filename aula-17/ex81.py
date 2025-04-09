lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    sn = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if sn == 'N':
        print('-='*30)
        print(f'Você digitou {len(lista)} valores')
        lista.sort(reverse=True)
        print(f'Aqui está seus valores em ordem decrescente: {lista}')
        if (5) not in lista:
            print('O valor 5 não está na lista')
        else:
            print('O valor 5 está na lista')
        break