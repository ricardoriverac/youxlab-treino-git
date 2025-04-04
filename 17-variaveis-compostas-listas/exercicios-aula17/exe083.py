paret = ['(' , ')']
expressao = str(input('Digite a expressão: '))
if paret[0] in expressao and paret[1] in expressao:
    print('Expressao valida!')
else:
    print('Expressão errada!')