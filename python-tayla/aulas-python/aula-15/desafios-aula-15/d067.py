numero = 0
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 18)
    if numero > 0:
        for multiplo in range(0, 11):
            print(f'{numero} x {multiplo} = {numero * multiplo}')
        print('-=' * 18)
    else:
        break
print('Tabuada encerrada. Volte Sempre!')