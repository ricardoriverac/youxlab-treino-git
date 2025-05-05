numero = int(input('Digite um número e descubra o seu fatorial: '))
counter = numero 
fatorar = 1 
print('Calculando...{}! ='.format(numero), end='')
while counter > 0:
    print('{}'.format(counter), end='')
    fatorar *= counter
    counter -= 1
    print('x' if counter > 1 else '=', end='')
    print('{}'.format(fatorar))