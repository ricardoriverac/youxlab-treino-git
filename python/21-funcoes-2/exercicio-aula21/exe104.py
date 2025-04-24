def leiaint(prompet=''):
    leia = str(input(prompet)).strip()
    while True:
        if leia.isnumeric():
            return f'{leia} \n'
        else:
            print('\033[31mERRO NÚMERO ERRADO! TENTE NOVAMENTE...\033[m')
            leia = str(input(prompet)).strip()


#programa principal
n = leiaint('Digite um número: ')
print(f'O número que você digitou é {n}')