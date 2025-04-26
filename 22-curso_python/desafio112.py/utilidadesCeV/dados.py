def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
    if entrada.isalpha():
        print(f'\033[3;31mERRO:\033[m{entrada} é um preço inválido.')
    else:
        valido = True
        return float(entrada)