def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isdigit() or (entrada.replace('.', '').isdigit() and entrada.count('.') == 1):
            return float(entrada)
        else:
            print(f'\033[31mERRO! {entrada} não é um preço válido!\033[m ')
