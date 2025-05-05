def hel(msg):

    while True:

        print('~'*40)

        print(f'ACESSANDO MANUAL DO COMANDO {msg} ')

        print('~' * 40)

        help(msg)

        print('~' * 40)

        print('  SISTEMA DE AJUDA PyHELP')

        print('~' * 40)

        msg = input('Função ou Biblioteca > ')

        if msg == 'fim':

            break





print('~'*40)

print('  SISTEMA DE AJUDA PyHELP')

print('~'*40)

msgg = input('Função ou Biblioteca > ')

hel(msgg)