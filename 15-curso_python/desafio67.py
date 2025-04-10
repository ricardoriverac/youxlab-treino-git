numeros = 0
negativo = 0
while True:
    print('-' * 20)
    print('\033[1;33mDigite um número negativo para encerrar o programa.\033[0;0m')
    numeros = int(input('Digite um número para ver sua tabuada: '))
    if numeros <= 0:
        print('Você encerrou o programa.')
        break
    for n in range (1, 11):
       resultado = numeros * n
       print(f'{numeros} x {n} = {resultado}')
print('OBRIGADA POR USAR O PROGRAMA.')


