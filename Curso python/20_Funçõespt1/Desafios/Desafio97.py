def escreva(msg):

    tam = len(msg)+8

    print('~'*tam)

    print(f'{msg:^{tam}}')

    print('~'*tam)



escreva('Espelho Vitral Azul e Vermelho') 