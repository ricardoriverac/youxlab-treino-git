

expressao = str(input('Digite sua explessao: '))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão correta!')
else:
    print('Expressão errada, você nao fechou os parenteses correntamente.')