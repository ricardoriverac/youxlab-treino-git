def leia_dinheiro():
    while True:
        num = input('Digite o preço (ex: 49.99): R$ ').strip().replace(',', '.')
        if num == '':
            print('\033[0;31mERRO: Entrada vazia. Por favor, digite um valor.\033[m')
            continue
        try:
            valor = float(num)
            if valor < 0:
                print(f'\033[0;31mERRO: "{num}" é um valor negativo. Digite um valor positivo.\033[m')
            else:
                return valor
        except ValueError:
            print(f'\033[0;31mERRO: "{num}" não é um número válido. Tente novamente.\033[m')
