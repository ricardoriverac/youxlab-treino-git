numero = 0
while numero >= 0:
    numero = int(input('Deseja ver a tabuada de qual valor? '))
    if numero >= 0:
        for tabuada in range(1, 11):
            resultado = numero * tabuada
            print (f'{numero} x {tabuada} = {resultado} ')
    if numero < 0:
        print ('Programa de tabuada encerrado. Volte sempre! ')
        break