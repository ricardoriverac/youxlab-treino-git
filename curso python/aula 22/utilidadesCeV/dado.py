def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido.\033[m')
        else:
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print(f'\033[31mERRO: "{entrada}" é um preço inválido.\033[m')
