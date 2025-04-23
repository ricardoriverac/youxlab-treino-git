def leiaDinheiro(pergunta):
    while True:
        n = float(input(pergunta))
        if type(n) == str:
            print(f'ERRO: {n} é um preço inválido')
        return n