def leia_cpf(msg="CPF: ", show=True):

    from time import sleep

    vad = False

    while not vad:

        erro = False
        c1 = input(msg).strip().replace('.', '').replace('-', '').replace(',', '')
        print('Verificando...')
        sleep(1)
        for c in range(0, len(c1)):
            if c1[c].isalpha():
                erro = True
        if len(c1) != 11:

            erro = True

        if erro:

            print(f'CPF inválido!')

        else:

            if show:
                print(f'O CPF \'{c1[:3]}.{c1[3:6]}.{c1[6:9]}-{c1[9:]}\' é válido.')
            else:
              print('CPF válido.')

            vad = True
            return int(c1)