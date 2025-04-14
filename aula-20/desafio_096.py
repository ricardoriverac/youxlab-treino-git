def metros2(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m².')

print('-'*40)
print(f'{"Controle de Terrenos":^40}')
print('-'*40)
largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
metros2(largura, comprimento)