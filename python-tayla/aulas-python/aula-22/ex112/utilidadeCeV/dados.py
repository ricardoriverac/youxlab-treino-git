def leiaDinheiro(mensagem):
    leiaValor = str(input(mensagem)).replace(',', '.')

    if '.' in leiaValor or leiaValor.isnumeric():
        leiaValor = float(leiaValor)
        return leiaValor
    else: 
        while True:
            print(f'\033[1;31mERRO! {leiaValor} é um preço inválido\033[m')
            leiaValor = str(input(mensagem)).replace(',', '.')
            if '.' in leiaValor or leiaValor.isnumeric():
                leiaValor = float(leiaValor)
                return leiaValor