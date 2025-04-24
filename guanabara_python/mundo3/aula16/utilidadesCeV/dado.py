def leiaDinheiro(msg):
    """
    Lê um valor monetário digitado pelo usuário com validação.
    Aceita números com vírgula ou ponto como separador decimal.
    Rejeita letras ou símbolos inválidos.
    """
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            if valor < 0:
                print('\033[1;31mERRO: O valor não pode ser negativo!\033[m')
            else:
                return valor
        except ValueError:
            print(f'\033[1;31mERRO: "{entrada}" não é um valor monetário válido!\033[m')
