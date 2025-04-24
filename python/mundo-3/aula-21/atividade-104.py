def leiaInt(msg):
    """
    Função que simula o input(), mas aceita apenas números inteiros válidos.
    """
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
