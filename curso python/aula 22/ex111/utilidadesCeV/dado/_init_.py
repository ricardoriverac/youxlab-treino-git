def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return numero

def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return numero

