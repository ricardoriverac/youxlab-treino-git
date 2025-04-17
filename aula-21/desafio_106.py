from time import sleep

cores = ('\033[m',          # 0 - sem cor
         '\033[7;30m',      # 1 - branco
         '\033[1;30;41m',   # 2 - vermelho
         '\033[1;30;42m',   # 3 - verde
         '\033[1;30;43m',   # 4 - amarelo
         '\033[1;30;44m',   # 5 - roxo
         '\033[1;30:45m',   # 6 - cinza
         '\033[1;30;46m',   # 7 - magenta
         '\033[1:30;47m',   # 8 - cinza
         )


def titulo(msg, cor=0):
    tam = len(msg) + 4

    sleep(0.5)

    print(f'{cores[cor]}-' * tam)
    print(f'{cores[cor]}{msg:^{tam}}')
    print(f'{cores[cor]}-' * tam)
    print(f'{cores[0]}')


def ajuda(comand, cor=0):

    sleep(0.5)

    print(f'{cores[cor]}')
    help(comand)
    print(f'{cores[0]}')


comando = ''

while True:

    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou biblioteca: '))

    if comando.upper() != 'FIM':

        ajuda(comando, 1)

    else:
        break

titulo('PROGRAMA FINALIZADO', 2)