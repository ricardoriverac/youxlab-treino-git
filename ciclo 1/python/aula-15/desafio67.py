while True:
    tabuada = int(input('Que ver a tabuada de qual valor? : '))
    contador = 1
    if tabuada < 0:
        break
    print('-'*40)
    while contador <= 10:
        print(f'{tabuada} x {contador} = {tabuada*contador}')
        contador += 1
    print('-' * 40)

print('FIM PROGRAMA TABUADA')
