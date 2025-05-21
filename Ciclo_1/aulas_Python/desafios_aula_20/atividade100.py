def solicitado():
    from random import sample

    lista = []

    numeros = list(range(0, 10))
    sam = sample(numeros, 5)
    lista.append(sam)
    print(f'Esses foram os valores sorteados: {sam}')

    par = 0
    imp = 0

    for num in sam:
        
        if num % 2 == 0:
            par += num
    print(f'A soma dos números pares é: {par}')
        
solicitado()
