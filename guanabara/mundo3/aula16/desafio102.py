def fatorial(num, show=False):
    """
    Calcula o fatorial de um número inteiro positivo.
    -> Parâmetros:
    num (int): O número inteiro do qual será calculado o fatorial. 
               Deve ser um número não-negativo.
    show (bool, opcional): Se True, a sequência de multiplicações é exibida 
                            durante o cálculo do fatorial. O valor padrão é False.

    Retorna:
    int: O resultado do fatorial do número fornecido.
    
    Exemplo:
    fatorial(5, show=True)
    # Saída: Calculando o fatorial de 5: 5 x 4 x 3 x 2 x 1 = 120 """

    resultado = 1
    if show:
        print(f"Calculando o fatorial de {num}: ", end="")
    for contador in range(num, 0, -1):
        resultado *= contador
        if show:
            print(contador, end="")
            if contador > 1:
                print(" x ", end="")
            else:
                print(f" = ", end="")
    return resultado


print(fatorial(5, show=True))