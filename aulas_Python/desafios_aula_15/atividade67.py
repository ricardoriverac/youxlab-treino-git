print('\033[1;34m-=-=-=-=-= Tabuada v3.0 =-=-=-=-=-\033[m')
c = 0
print('\033[1;34m-=-=-=-=-= Digite algum número negativo para encerrar o programa (ex: -1, -2, -3...) =-=-=-=-=-\033[m')
while True:
    numero = int(input('Qual número você quer ver a tabuada? '))
    if numero > 0:
        for c in range(0, 11,):
            mul = c*numero
            print(f'{numero} x {c} = {mul}')
    elif numero < 0:
        break