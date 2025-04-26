def fatorial(numero, show=False):
    if show:
        counter = numero 
        fatorar = 1 
        print('Calculando...{}! =\n'.format(numero), end='')
        while counter > 0:
            print('{}'.format(counter), end='')
            fatorar *= counter
            counter -= 1
            print(' x ' if counter > 0 else ' = ', end='')
        print('{}'.format(fatorar))
 
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        print(f'O fatorial de {numero} é: {fatorial}')
        
# numero = int(input('Digite um número e descubra o seu fatorial: '))
print(fatorial(5, True))