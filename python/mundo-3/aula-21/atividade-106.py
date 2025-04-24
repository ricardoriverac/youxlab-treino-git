def ajuda(comando):
    titulo(f"Acessando o manual do comando '{comando}'", cor=4)
    print('\033[7;40m', end='')  # Fundo branco
    help(comando)
    print('\033[m', end='')


def titulo(msg, cor=0):
    cores = [
        '\033[m',         # 0 - Sem cor
        '\033[0;30;41m',  # 1 - Vermelho
        '\033[0;30;42m',  # 2 - Verde
        '\033[0;30;43m',  # 3 - Amarelo
        '\033[0;30;44m',  # 4 - Azul
        '\033[0;30;45m',  # 5 - Roxo
    ]
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print('\033[m', end='')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', cor=1)
        break
    else:
        ajuda(comando)
