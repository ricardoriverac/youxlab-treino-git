def leiaInt(Mensagem):
    ValorValido = False
    while True:
        Entrada = input(Mensagem)
        if Entrada.isnumeric():
            Numero = int(Entrada)
            ValorValido = True
        else:
            print('\033[31mDigite um número inteiro válido.\033[m')
        if ValorValido:
            break
    return Numero
NumeroDigitado = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {NumeroDigitado}.')
