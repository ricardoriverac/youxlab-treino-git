def leia_num(msg, tipo):
    """
    Lê um número do tipo especificado (int ou float), com validação e interação com o usuário.
    
    :param msg: Mensagem a ser exibida para o usuário
    :param tipo: Tipo do número esperado (int ou float)
    :return: Valor convertido para o tipo desejado
    """
    if tipo == float:
        t = "real"
    elif tipo == int:
        t = "inteiro"
    else:
        print('\033[31mERRO! Tipo de dado inválido. Use int ou float.\033[m')
        return None

    while True:
        entrada = input(msg).strip().replace(',', '.')
        
        if entrada == '':
            print(f'\033[31mERRO! Entrada vazia. Digite um número {t} válido.\033[m')
            continue

        try:
            n = tipo(entrada)
            print(f'Você digitou o número {t}: {n}')
            return n
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número {t} válido.\033[m')
