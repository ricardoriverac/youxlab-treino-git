cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
         'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ''
total = 0
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if 0 > número:
        print('Tente novamente! ', end='')
    elif 20 < número:
        print('Tente novamente! ', end='')
    if 0 <= número <= 20:
        print(f'Você escolheu o número {cont[número]}.')
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        total += 1
        if continuar == 'N':
            break
print(f'Você escolheu {total} vezes os números da tupla')
print('Volte sempre!')