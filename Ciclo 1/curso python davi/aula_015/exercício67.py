print('tabela de multiplicação')
count = number = 0
while True:
    number = int(input('digite um número '))
    if number < 0:
        break
    for n in range (1, 11):
        print(f'{number} X {n} = {number * n}')