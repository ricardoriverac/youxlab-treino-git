def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mEROO: \"{entrada}\" é um número inválido!\033[m')
            
        else:
            valido = True
            return float(entrada)