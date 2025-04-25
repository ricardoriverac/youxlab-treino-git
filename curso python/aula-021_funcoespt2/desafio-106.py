from time import sleep
def manual(comando):
    print(f'Acessando a biclioteca de {comando}')
    for c in range(5):
        print('.', end='')
        sleep(0.5)
    help(comando)


while True:
    com = str(input('Qual comando você deseja ver? (FIM, para o programa)'))
    manual(com)
    if com == 'fim':
        break