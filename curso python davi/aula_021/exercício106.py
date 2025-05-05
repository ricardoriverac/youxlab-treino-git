def ajuda(comando):
    """
    Mostra o manual do comando com destaque de cores.
    """
    titulo(f"Acessando o manual do comando '{comando}'", cor=4)
    print('\033[7;40m', end='')
    help(comando)
    print('\033[m', end='')


def titulo(msg, cor=0):
    """
    Exibe um título centralizado com cores.

    Cores:
    0 = branco, 1 = vermelho, 2 = verde, 3 = amarelo, 4 = azul, 5 = roxo, 6 = ciano
    """
    cores = [
        '\033[m',
        '\033[31m',
        '\033[32m',     
        '\033[33m',     
        '\033[34m',     
        '\033[35m',
        '\033[36m'
    ]
    print(cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print('\033[m', end='')
while True:
    titulo("SISTEMA DE AJUDA PyHelp", cor=2)
    comando = input("Função ou biblioteca (ou 'fim' para sair): ").strip().lower()
    if comando == 'fim':
        titulo("ATÉ LOGO!", cor=1)
        break
    else:
        ajuda(comando)