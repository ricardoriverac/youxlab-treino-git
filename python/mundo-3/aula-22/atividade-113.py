def leiaInt(msg):
    """
    Função que simula o input(), mas aceita apenas números inteiros válidos.
    """
    while True:
        try:
            n = input(msg)
            if n.strip() == '':
                raise ValueError
            n = int(n)
            return n
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')


def leiaFloat(msg):
    """
    Função que simula o input(), mas aceita apenas números reais válidos.
    """
    while True:
        try:
            n = input(msg)
            if n.strip() == '':
                raise ValueError
            n = float(n)
            return n
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número real válido.\033[m')

num_int = leiaInt('Digite um número inteiro: ')
num_float = leiaFloat('Digite um número real: ')
print(f'Você digitou o inteiro {num_int} e o real {num_float}.')
