def leiaInt():
    while True:
        num = input('Digite um valor')
             
        try:
            num = int(num)
            print(f'O valor {num} é aceito')
            return num

        except ValueError:
            print(f'Erro o valor é uma string. ')



leiaInt()
