from time import sleep
c = [
    '\033[m',
    '\033[0;30;41m',
    '\033[0;30;42m',
    '\033[0;30;43m', 
    '\033[0;30;44m', 
    '\033[0;30;45m', 
    '\033[7;30m']

def ajuda(coman):
    titulo(f'Acessando o manual do comando \'{coman}\'', 4)
    print(c[6], end='')
    help(coman)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor = 0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'   {msg}   ')
    print('~' * tamanho)
    print(c[0], end = '')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('VOLTE SEMPRE! ', 1)

