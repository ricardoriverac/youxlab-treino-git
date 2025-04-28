def ajuda(com):
    help(com)

def titulo(mensagem):
    tamanho = len(mensagem)

    print('~'*tamanho)
    print(f'  {mensagem}')
    print('~'*tamanho)



comando = ''

while True:
    titulo('Sistema de ajuda PyHelp')

    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break 

    else:
        ajuda(comando) 
titulo('Até daqui a pouco! ')