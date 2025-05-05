def leiaint():

    n = str(input('Digite um número: '))

    while not n.isnumeric():

        print('Ops! Apenas números são aceitos!')

        n = str(input('Digite um número: '))

    if n.isnumeric():

        n = int(n)

        print(f'Você digitou o número: {n} ')





leiaint()