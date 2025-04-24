paret = ['(' , ')']
expressao = str(input('Digite a expressão: '))
if paret[0] in expressao and paret[1] in expressao: 
    print('Expressao valida!')
if paret[0] not in expressao and paret[1] not in expressao :
    print('Expressão errada!')