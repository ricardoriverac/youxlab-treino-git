def leiaDinheiro(dados):

    valido = False
    while not valido:
        entrada = str(input(dados)).replace(',','.')  

        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro {entrada} e um preço invalido ')

        else:
            valido = True
            return float(entrada)
        