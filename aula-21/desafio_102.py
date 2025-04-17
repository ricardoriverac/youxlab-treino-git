def fatorial(num, show=False):
    """
    -> Calcula o fatorial do número digitado.
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """
    if show:
        multiplicador = 1
        print('-' * 20)
        for numero in range(num, 0, -1):
            multiplicador *= numero
            print(numero, end='')
            print(' x ' if numero > 1 else ' = ', end='')
        return multiplicador
    else:
        multiplicador = 1
        print('-' * 20)
        for numero in range(num, 0, -1):
            multiplicador *= numero
        return multiplicador

print(fatorial(1, True))
