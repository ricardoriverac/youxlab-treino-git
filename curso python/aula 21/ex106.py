from time import sleep
def ajuda(Comando):
    mostrarTitulo(f'Acessando o manual do comando \'{Comando}\'', 4)
    print(Cores[6], end='')
    help(Comando)
    print(Cores[0], end='')
    sleep(2)
    
def mostrarTitulo(Mensagem, Cor=0):
    Tamanho = len(Mensagem) + 4
    print(Cores[Cor], end='')
    print('~' * Tamanho)
    print(f'  {Mensagem}')
    print('~' * Tamanho)
    print(Cores[0], end='')
    sleep(1)
Cores = [
    '\033[m',        
    '\033[0;30;41m', 
    '\033[0;30;42m', 
    '\033[0;30;43m', 
    '\033[0;30;44m', 
    '\033[0;30;45m', 
    '\033[7;30m'     
]

Comando = ''
while True:
    mostrarTitulo('SISTEMA DE AJUDA PyHELP', 2)
    Comando = str(input('Função ou Biblioteca > '))
    if Comando.upper() == 'FIM':
        break
    else:
        ajuda(Comando)
mostrarTitulo('ATÉ LOGO!', 1)
