cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n1 = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n1 <= 10:
        print(f'O número digitado foi {cont[n1]}')
    else:
        print('Tente de novo, zé. ', end='')
        continue

    responda = ' '
    while responda not in 'SN':
        responda = input('Você quer continuar? [S/N] ').strip().upper()[0]

    if responda == 'N':
        break
