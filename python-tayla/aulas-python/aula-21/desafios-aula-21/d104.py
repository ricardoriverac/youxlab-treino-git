def leiaInt(mensagem):
    while True:
        numero = input(mensagem)

        if numero.isdigit():
            print(f'Você acabou de digitar o número {numero}')
            return int(numero)
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
    
leiaInt('Digite um número: ')