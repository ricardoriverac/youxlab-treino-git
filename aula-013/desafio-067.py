isRodando = True
while isRodando:
    num = int(input('Digite o número para ver sua tabuada: '))
    if num < 0:
        print('FIM')
        break
    else:
        for c in range (1, 10 +1):
            tabuada = num * c
            print(f'{num} x {c} = {tabuada}')
    