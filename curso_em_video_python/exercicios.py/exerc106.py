def ajuda(c):
    help(c)

def texto(m, cor=0):
    tamanho = len(m)
    print('=' * tamanho)
    print(f'\033[1;33m{m}\033[m')
    print('=' * tamanho)

print('\033[3;37mdigite FIM para interromper.\033[m')
escolha = ''
while True:
    texto('SISTEMA DE AJUDA')
    escolha = str(input('Digite uma função: '))
    if escolha.upper() == 'FIM':
        break
    else:
        ajuda(escolha)

