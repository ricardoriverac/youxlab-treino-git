def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print(f'ERRO: "{entrada}" não é um valor válido.')
