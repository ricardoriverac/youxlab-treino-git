def maior(* num):
    contador = maior = 0
    for i in num:
        if i > maior:
            maior = i
        contador += 1
        print(f'{i}', end=' ')
    print()
    if contador == 0:
        print('Não haviam números para serem analisados. ')
    else:
        print(f'Foram analisados {contador} números e o maior foi {maior}')
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()