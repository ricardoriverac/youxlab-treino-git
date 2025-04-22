def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    Parâmetros:
    n -- número inteiro para o cálculo do fatorial
    show -- (opcional) mostra ou não o processo de cálculo

    Retorna:
    O valor do fatorial de n
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f

print(fatorial(5))       
print(fatorial(5, show=True))  