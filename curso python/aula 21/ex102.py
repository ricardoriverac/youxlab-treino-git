def fatorial(Numero, Mostrar=False):
    """
    Calcula o fatorial de um número inteiro.
    Parâmetros:
    Numero: número a ser calculado.
    Mostrar: se True, mostra o processo do cálculo.
    Retorna:
    O valor do fatorial do número.
    """
    Resultado = 1
    for Contador in range(Numero, 0, -1):
        if Mostrar:
            print(Contador, end='')
            if Contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        Resultado *= Contador
    if Mostrar:
        print(Resultado)
        return ''
    else:
        return Resultado
print(fatorial(5, Mostrar=True))
