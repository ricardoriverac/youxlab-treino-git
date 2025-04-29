def t106():
    import time 
    print('\033[41mAtenção!! o comando "fim" encerra o programa\033[0m')
    while True:
        
        print(f"\033[42m{'~' * 23}\033[0m")
        print("\033[42mSISTEMA DE AJUDA PyHELP\033[0m")
        print(f"\033[42m{'~' * 23}\033[0m")
        
        ForB = input('Digite uma Função ou Biblioteca: ')
        
        if ForB.lower() == 'fim':
            print(f"\033[41m{'~' * 13}\033[0m")
            print("\033[41mEncerrando...\033[0m")
            print(f"\033[41m{'~' * 13}\033[0m")
            time.sleep(1)
            break
        
        linha = '~' * len(f'Acessando o manual do comando {ForB}')
        print(f'\033[48;5;123m{linha}\033[0m')
        print(f'\033[48;5;123mAcessando o manual do comando {ForB}\033[0m')
        print(f'\033[48;5;123m{linha}\033[0m')
        time.sleep(1)
        print(f'\033[48;5;255m{help(ForB)}\033[0m')

t106()