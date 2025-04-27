def leiIntFlo():
    while True:
        try:
            numero1 = int(input('Digite um número inteiro: '))
        except ValueError:
            print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
        else:
            break
    while True:
            entrada = (input('Digite um número real: ')).strip()
            if entrada == '':
                numero2 = 0.0
                print('\nO usuario preferiu não informar um número real')
                break
            try:
                numero2 = float(entrada)
                break
            except ValueError:
             print('\033[31mErro: Por favor, digite um número real válido.\033[m')
    
    print('-'*20)
    print(f'Número iteiro {numero1} | Número real {numero2}')
    

leiIntFlo()