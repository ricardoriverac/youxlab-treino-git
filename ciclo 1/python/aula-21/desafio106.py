from time import sleep

cores = ('\033[m',          # 0 - sem cor
         '\033[7;30m',      # 1 - branco
         '\033[1;30;41m',   # 2 - vermelho
         '\033[1;30;42m',   # 3 - verde
         '\033[1;30;43m',   # 4 - amarelo
         '\033[1;30;44m',   # 5 - azul
         '\033[1;30;45m',   # 6 - roxo
         '\033[1;30;46m',   # 7 - ciano
         '\033[1;30;47m',   # 8 - cinza claro
        )

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor] + '-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam + cores[0])
    sleep(1)

def ajuda(comando, cor=0):
    print(cores[cor])
    help(comando)
    print(cores[0])
    sleep(1)

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = input('Função ou biblioteca ("FIM" para sair): ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando, 1)

titulo('PROGRAMA FINALIZADO', 2)
