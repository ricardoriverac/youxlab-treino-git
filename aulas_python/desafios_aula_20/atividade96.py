def mensagem(txt):
    print('-'*20)
    print(txt)
    print('-'*20)
mensagem('Controle de Terrenos')
mensagem

def calculo(a, b):
    c = a * b
    print('=-='*15)
    print(f'A área de um terreno {a} X {b} é de {c}m².')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

calculo(largura, comprimento)