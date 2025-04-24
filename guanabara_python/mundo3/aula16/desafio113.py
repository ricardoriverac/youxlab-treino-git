def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero
        except ValueError:
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'\nVocê digitou o número inteiro {inteiro} e o número real {real:.2f}')