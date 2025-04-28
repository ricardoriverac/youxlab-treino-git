def maior():
    num1 = []
    print('Digite 999 para parar o programa.')
    while True:
        num = int(input('Digite um valor: '))
        if num == 999:
            break
        num1.append(num)
    if num1:
        print(f'O maior valor digitado foi {max(num1)}')
    else:
        print('Nenhum valor foi digitado.')

maior()
