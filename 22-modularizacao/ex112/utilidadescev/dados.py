def leiadinheiro(msg=''):
    leia = str(input(msg)).replace(',','.')
    if '.' in leia or leia.isnumeric():
        leia = float(leia)
        return leia
    else:
        while True:
            print('\033[31mERRO! TENTE NOVAMENTE!\033[m')
            leia = str(input(msg)).replace(',','.')
            if '.' in leia or leia.isnumeric():
                leia = float(leia)
                return leia
